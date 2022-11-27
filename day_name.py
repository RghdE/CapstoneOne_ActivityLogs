
# importing the libraries neeeded for the python file
from mrjob.job import MRJob
from mrjob.step import MRStep

# define the class name and passing MRJob obj to the class 
class day_name(MRJob):

    # define the number of steps? (similir to the pipline) 
    # when I removed this function, the code didnt work for me
    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_day,
                   reducer=self.reducer_sum_day),
            MRStep(reducer=self.reducer_sorted_output)
        ]
    
    # the map step: each line in the txt file is read as a key, value pair
    # in this case, each line in the txt file contains multiple values, one of them is (the record itself: industry name), but no key
    # _ means that in this case, there is no key for each line
    def mapper_get_day(self, _, line):

        # identifying the columns and by which they're seperated 
        (ID, session_id, Type, window_id, browser, device_type, os, host, current_url, referrer, referring_domain, pathname,
         path1, path2, path3, path4, path5, number_of_pages, event_type, date, year, month, day, month_name, day_name, 
         week_label, time, day_parts, browser_version, screen_height, screen_width, viewport_height, viewport_width, 
         min_time, max_time, duration_hours, duration_minutes, duration_seconds, total_pages, invest) = line.split('\t')
        # identify the column we're interested in to take it as a key
        yield day_name, 1


    # the reduce step: combine all tuples with the same key (industry name)
    # then sum all the values of the tuple, which will give the average duration time for all the sessions
    def reducer_sum_day(self, key, values):
        yield sum(values), key

    def reducer_sorted_output(self, count, days):
        for d in days:
            yield d, count

# calling main function to run the file
if __name__ == '__main__':
    day_name.run()
