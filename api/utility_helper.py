from datetime import datetime, timezone, timedelta
import calendar


########################################################################################################
#### Added By: SHIFULLAH 
#### time difference
########################################################################################################
class TimeCalculation:
    def time_difference(stime, etime):
        """ 
            Args:
                    start_time and end_time

            Returns:
                time_difference
        """
        
        try:
            start_time = datetime.strptime(stime, "%Y-%m-%dT%H:%M:%S.%fZ") 
        except:
            start_time = datetime.strptime(stime, "%Y-%m-%dT%H:%M:%SZ")

        try:
            end_time = datetime.strptime(etime, "%Y-%m-%dT%H:%M:%S.%fZ")
        except:
            end_time = datetime.strptime(etime, "%Y-%m-%dT%H:%M:%SZ") 

        # get difference
        delta = end_time - start_time 
        sec = delta.total_seconds() 

        min = sec / 60
        # print('difference in minutes:', min)

        # get difference in hours
        hours = sec / (60 * 60)
        # print('difference in hours:', hours)

        return hours

    def week_work_time(current_day):
        """ 
            Args:
                    today

            Returns:
                date range of week
        """
        
        if current_day == 'Monday':
            sdate = datetime.now().date() - timedelta(days=0)
            edate = datetime.now().date() + timedelta(days=6)
            return [sdate, edate]
        elif current_day == 'Tuesday':
            sdate = datetime.now().date() - timedelta(days=1)
            edate = datetime.now().date() + timedelta(days=5)
            return [sdate, edate]
        elif current_day == 'Wednesday':
            sdate = datetime.now().date() - timedelta(days=2)
            edate = datetime.now().date() + timedelta(days=4)
            return [sdate, edate]
        elif current_day == 'Thursday':
            sdate = datetime.now().date() - timedelta(days=3)
            edate = datetime.now().date() + timedelta(days=3)
            return [sdate, edate]
        elif current_day == 'Friday':
            sdate = datetime.now().date() - timedelta(days=4)
            edate = datetime.now().date() + timedelta(days=2)
            return [sdate, edate]
        elif current_day == 'Saturday':
            sdate = datetime.now().date() - timedelta(days=5)
            edate = datetime.now().date() + timedelta(days=1)
            return [sdate, edate]
        elif current_day == 'Sunday':
            sdate = datetime.now().date() - timedelta(days=6)
            edate = datetime.now().date() + timedelta(days=0)
            return [sdate, edate]

    def month_work_time():
        """ 
            Args:
                    None

            Returns:
                date range of current month
        """
        today = datetime.now().date() 

        curr_year = today.year 
        curr_month = today.month 
        month_range = calendar.monthrange(curr_year, curr_month)  
        
        sdate = datetime(curr_year, curr_month, 1).date() 
        edate = datetime(curr_year, curr_month, month_range[1]).date() 
        return [sdate, edate]


