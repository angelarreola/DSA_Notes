class Solution:
    def numberOfRounds(self, loginTime: str, logoutTime: str) -> int:
        loginTimeArray = loginTime.split(":")
        logoutTimeArray = logoutTime.split(":")
        
        loginHour = int(loginTimeArray[0])
        logoutHour = int(logoutTimeArray[0])
        loginMinutes = int(loginTimeArray[1])
        logoutMinutes = int(logoutTimeArray[1])
        
        if logoutHour < loginHour:
            playedHoursToMinutes = ((24 - loginHour) + logoutHour) * 60
        elif logoutHour == loginHour and loginMinutes >= logoutMinutes:
            playedHoursToMinutes = 24 * 60
        else:
            playedHoursToMinutes = (logoutHour - loginHour) * 60
        
        extraMinutes = (logoutMinutes % 15)
        realPlayedMinutes = playedHoursToMinutes - loginMinutes - extraMinutes + logoutMinutes
        
        print(f"played = {realPlayedMinutes}")
        print("------------------------")
        
        if realPlayedMinutes >= 15:
            return realPlayedMinutes // 15
        return 0
        
        
    

s = Solution()
loginTime = "00:47"
logoutTime = "00:57"
ans = s.numberOfRounds(loginTime, logoutTime)
print(ans)  