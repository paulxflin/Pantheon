class Solution:
    # Split + List for month + checking digits (Accepted), O(1) time and space
    def reformatDate(self, date: str) -> str:
        day, month, year = date.split()
        if day[1].isdigit():
            day = day[:2]
        else:
            day = '0' + day[0]

        months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
                  "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        month = months.index(month) + 1
        if month < 10:
            month = '0' + str(month)
        else:
            month = str(month)

        return year + '-' + month + '-' + day

    # Dict for months + check len (Top Voted), O(1) time and space
    def reformatDate(self, date: str) -> str:
        M = {"Jan": "01", "Feb": "02", "Mar": "03", "Apr": "04", "May": "05", "Jun": "06",
             "Jul": "07", "Aug": "08", "Sep": "09", "Oct": "10", "Nov": "11", "Dec": "12", }

        D = ""
        if (len(date) == 13):
            D += date[-4:] + "-" + M[date[-8:-5]] + "-" + date[:2]
        else:
            D += date[-4:] + "-" + M[date[-8:-5]] + "-0" + date[0]
        return D
