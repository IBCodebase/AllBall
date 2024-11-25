import time
from bs4 import BeautifulSoup
import requests

class PlayerStatTools:

    def findPage(playerName):
        url = "https://www.basketball-reference.com/"
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        form = soup.find("form", {"name": "f_big"})
        action = form["action"]
        method = form["method"].lower()

        base_url = "https://www.basketball-reference.com"

        params = {
            "search": playerName,
            "pid": "",
            "idx": ""
        }

        response = requests.get(f"{base_url}{action}", params=params)
        possibleLinks = []
        if response.status_code == 200:
            responseArray = response.text.split("\n")
            for line in responseArray:
                if line.__contains__("<div class=\"search-item-url\">/players/"):
                    urlLine = line.split(">")[1].split("<")[0]
                    possibleLinks.append(base_url + urlLine)
        else:
            print("Failed to fetch the page:", response.status_code)
        return requests.get(possibleLinks[0]).text

    def statsPulloutExtractorSeason(dataTipName, htmlString):
        needXlines = 0;
        returnLine = ""
        htmlArray = htmlString.split("\n")

        for line in htmlArray:
            if line.__contains__("<span class=\"poptip\" data-tip=\"" + dataTipName):
                needXlines = 1
            if needXlines > 0:
                returnLine = line
                needXlines = needXlines - 1
        return returnLine.split("<p>")[1].split("</p>")[0]

    def statsPulloutExtractorCareer(dataTipName, htmlString):
        needXlines = 0;
        returnArr = []
        htmlArray = htmlString.split("\n")
        for line in htmlArray:
            if line.__contains__("<span class=\"poptip\" data-tip=\"" + dataTipName):
                needXlines = 2
            if needXlines > 0:
                returnArr.append(line)
                needXlines = needXlines - 1
        return returnArr[1].split("<p>")[1].split("</p>")[0]

    def getRecentSeasonGames(playerName):
        html = PlayerStatTools.findPage(playerName)
        return PlayerStatTools.statsPulloutExtractorSeason("Games", html)

    def getRecentSeasonGamesHtml(html):
        return PlayerStatTools.statsPulloutExtractorSeason("Games", html)

    def getCareerGames(playerName):
        html = PlayerStatTools.findPage(playerName)
        return PlayerStatTools.statsPulloutExtractorCareer("Games", html)

    def getCareerGames(html):
        return PlayerStatTools.statsPulloutExtractorCareer("Games", html)

    def getRecentSeasonPoints(playerName):
        html = PlayerStatTools.findPage(playerName)
        return PlayerStatTools.statsPulloutExtractorSeason("Points", html)

    def getRecentSeasonPointsHtml(html):
        return PlayerStatTools.statsPulloutExtractorSeason("Points", html)

    def getCareerPoints(playerName):
        html = PlayerStatTools.findPage(playerName)
        return PlayerStatTools.statsPulloutExtractorCareer("Points", html)

    def getCareerPointsHtml(html):
        return PlayerStatTools.statsPulloutExtractorCareer("Points", html)

    def getRecentSeasonTotalRebounds(playerName):
        html = PlayerStatTools.findPage(playerName)
        return PlayerStatTools.statsPulloutExtractorSeason("Total Rebounds", html)

    def getRecentSeasonTotalReboundsHtml(html):
        return PlayerStatTools.statsPulloutExtractorSeason("Total Rebounds", html)

    def getCareerTotalRebounds(playerName):
        html = PlayerStatTools.findPage(playerName)
        return PlayerStatTools.statsPulloutExtractorCareer("Total Rebounds", html)

    def getCareerTotalReboundsHtml(html):
        return PlayerStatTools.statsPulloutExtractorCareer("Total Rebounds", html)

    def getRecentSeasonAssists(playerName):
        html = PlayerStatTools.findPage(playerName)
        return PlayerStatTools.statsPulloutExtractorSeason("Assists", html)

    def getRecentSeasonAssistsHtml(html):
        return PlayerStatTools.statsPulloutExtractorSeason("Assists", html)

    def getCareerAssists(playerName):
        html = PlayerStatTools.findPage(playerName)
        return PlayerStatTools.statsPulloutExtractorCareer("Assists", html)

    def getCareerAssistsHtml(html):
        return PlayerStatTools.statsPulloutExtractorCareer("Assists", html)

    def getRecentSeasonFGP(playerName):
        html = PlayerStatTools.findPage(playerName)
        return PlayerStatTools.statsPulloutExtractorSeason("Field Goal Percentage", html)

    def getRecentSeasonFGPHtml(html):
        return PlayerStatTools.statsPulloutExtractorSeason("Field Goal Percentage", html)

    def getCareerFGP(playerName):
        html = PlayerStatTools.findPage(playerName)
        return PlayerStatTools.statsPulloutExtractorCareer("Field Goal Percentage", html)

    def getCareerFGPHtml(html):
        return PlayerStatTools.statsPulloutExtractorCareer(html)

    def getRecentSeason3PointFGP(playerName):
        html = PlayerStatTools.findPage(playerName)
        return PlayerStatTools.statsPulloutExtractorSeason("3-Point Field Goal Percentage", html)

    def getRecentSeason3PointFGPHtml(html):
        return PlayerStatTools.statsPulloutExtractorSeason("3-Point Field Goal Percentage", html)

    def getCareer3PointFGP(playerName):
        html = PlayerStatTools.findPage(playerName)
        return PlayerStatTools.statsPulloutExtractorCareer("3-Point Field Goal Percentage", html)

    def getCareer3PointFGPHtml(html):
        return PlayerStatTools.statsPulloutExtractorCareer("3-Point Field Goal Percentage", html)

    def getRecentSeasonFTP(playerName):
        html = PlayerStatTools.findPage(playerName)
        return PlayerStatTools.statsPulloutExtractorSeason("Free Throw Percentage", html)

    def getRecentSeasonFTPHtml(html):
        return PlayerStatTools.statsPulloutExtractorSeason("Free Throw Percentage", html)

    def getCareerFTP(playerName):
        html = PlayerStatTools.findPage(playerName)
        return PlayerStatTools.statsPulloutExtractorCareer("Free Throw Percentage", html)

    def getCareerFTPHtml(html):
        return PlayerStatTools.statsPulloutExtractorCareer("Free Throw Percentage", html)

    def getRecentSeasonEFTP(playerName):
        # weird input for extractor because the html coder was inconsistent on web page
        # i.e. blame them
        html = PlayerStatTools.findPage(playerName)
        return PlayerStatTools.statsPulloutExtractorSeason("<strong>Effective Field Goal Percentage", html)

    def getRecentSeasonEFTPHtml(html):
        # weird input for extractor because the html coder was inconsistent on web page
        # i.e. blame them
        return PlayerStatTools.statsPulloutExtractorSeason("<strong>Effective Field Goal Percentage", html)

    def getCareerEFTP(playerName):
        # weird input for extractor because the html coder was inconsistent on web page
        # i.e. blame them
        html = PlayerStatTools.findPage(playerName)
        return PlayerStatTools.statsPulloutExtractorCareer("<strong>Effective Field Goal Percentage", html)

    def getCareerEFTPHtml(html):
        # weird input for extractor because the html coder was inconsistent on web page
        # i.e. blame them
        return PlayerStatTools.statsPulloutExtractorCareer("<strong>Effective Field Goal Percentage", html)

    def applyMethodToGroup(methodCode, playerArray, waitTime):
        # recomended waitTime (time in between requests) for this method is 6 second (website limits to 10 requests per

        # This method uses codes to indicate what method you would like to run on a list of
        # players, the codes go as follows
        # 1 = getRecentSeasonGames
        # 2 = getCareerGames
        # 3 = getRecentSeasonPoints
        # 4 = getCareerPoints
        # 5 = getRecentSeasonTotalRebounds
        # 6 = getCareerTotalRebounds
        # 7 = getRecentSeasonAssists
        # 8 = getCareerAssists
        # 9 = getRecentSeasonFGP
        # 10 = getCareerFGP
        # 11 = getRecentSeason3PointFGP
        # 12 = getCareer3PointFGP
        # 13 = getRecentSeasonFGP
        # 14 = getCareerFGP
        # 15 = getRecentSeasonEFGP
        # 16 = getCareerEFGP

        returnArray = []
        if (methodCode == 1):
            for player in playerArray:
                returnArray.append(PlayerStatTools.getRecentSeasonGames(player))
                time.sleep(waitTime)
            return returnArray
        if (methodCode == 2):
            for player in playerArray:
                returnArray.append(PlayerStatTools.getCareerGames(player))
                time.sleep(waitTime)
            return returnArray
        if (methodCode == 3):
            for player in playerArray:
                returnArray.append(PlayerStatTools.getRecentSeasonPoints(player))
                time.sleep(waitTime)
            return returnArray
        if (methodCode == 4):
            for player in playerArray:
                returnArray.append(PlayerStatTools.getCareerPoints(player))
                time.sleep(waitTime)
            return returnArray
        if (methodCode == 5):
            for player in playerArray:
                returnArray.append(PlayerStatTools.getRecentSeasonTotalRebounds(player))
                time.sleep(waitTime)
            return returnArray
        if (methodCode == 6):
            for player in playerArray:
                returnArray.append(PlayerStatTools.getCareerTotalRebounds(player))
                time.sleep(waitTime)
            return returnArray
        if (methodCode == 7):
            for player in playerArray:
                returnArray.append(PlayerStatTools.getRecentSeasonAssists(player))
                time.sleep(waitTime)
            return returnArray
        if (methodCode == 8):
            for player in playerArray:
                returnArray.append(PlayerStatTools.getCareerAssists(player))
                time.sleep(waitTime)
            return returnArray
        if (methodCode == 9):
            for player in playerArray:
                returnArray.append(PlayerStatTools.getRecentSeasonFGP(player))
                time.sleep(waitTime)
            return returnArray
        if (methodCode == 10):
            for player in playerArray:
                returnArray.append(PlayerStatTools.getCareerFGP(player))
                time.sleep(waitTime)
            return returnArray
        if (methodCode == 11):
            for player in playerArray:
                returnArray.append(PlayerStatTools.getRecentSeason3PointFGP(player))
                time.sleep(waitTime)
            return returnArray
        if (methodCode == 12):
            for player in playerArray:
                returnArray.append(PlayerStatTools.getCareer3PointFGP(player))
                time.sleep(waitTime)
            return returnArray
        if (methodCode == 13):
            for player in playerArray:
                returnArray.append(PlayerStatTools.getRecentSeasonFTP(player))
                time.sleep(waitTime)
            return returnArray
        if (methodCode == 14):
            for player in playerArray:
                returnArray.append(PlayerStatTools.getCareerFTP(player))
                time.sleep(waitTime)
            return returnArray
        if (methodCode == 15):
            for player in playerArray:
                returnArray.append(PlayerStatTools.getRecentSeasonEFTP(player))
                time.sleep(waitTime)
            return returnArray
        if (methodCode == 16):
            for player in playerArray:
                returnArray.append(PlayerStatTools.getCareerEFTP(player))
                time.sleep(waitTime)
            return returnArray

    def applyMethodToGroupHtmlArray(methodCode, htmlArray):
        returnArray = []
        if (methodCode == 1):
            for html in htmlArray:
                returnArray.append(PlayerStatTools.getRecentSeasonGames(html))
            return returnArray
        if (methodCode == 2):
            for html in htmlArray:
                returnArray.append(PlayerStatTools.getCareerGames(html))
            return returnArray
        if (methodCode == 3):
            for html in htmlArray:
                returnArray.append(PlayerStatTools.getRecentSeasonPoints(html))
            return returnArray
        if (methodCode == 4):
            for html in htmlArray:
                returnArray.append(PlayerStatTools.getCareerPoints(html))
            return returnArray
        if (methodCode == 5):
            for html in htmlArray:
                returnArray.append(PlayerStatTools.getRecentSeasonTotalRebounds(html))
            return returnArray
        if (methodCode == 6):
            for html in htmlArray:
                returnArray.append(PlayerStatTools.getCareerTotalRebounds(html))
            return returnArray
        if (methodCode == 7):
            for html in htmlArray:
                returnArray.append(PlayerStatTools.getRecentSeasonAssists(html))
            return returnArray
        if (methodCode == 8):
            for html in htmlArray:
                returnArray.append(PlayerStatTools.getCareerAssists(html))
            return returnArray
        if (methodCode == 9):
            for html in htmlArray:
                returnArray.append(PlayerStatTools.getRecentSeasonFGP(html))
            return returnArray
        if (methodCode == 10):
            for html in htmlArray:
                returnArray.append(PlayerStatTools.getCareerFGP(html))
            return returnArray
        if (methodCode == 11):
            for html in htmlArray:
                returnArray.append(PlayerStatTools.getRecentSeason3PointFGP(html))
            return returnArray
        if (methodCode == 12):
            for html in htmlArray:
                returnArray.append(PlayerStatTools.getCareer3PointFGP(html))
            return returnArray
        if (methodCode == 13):
            for html in htmlArray:
                returnArray.append(PlayerStatTools.getRecentSeasonFTP(html))
            return returnArray
        if (methodCode == 14):
            for html in htmlArray:
                returnArray.append(PlayerStatTools.getCareerFTP(html))
            return returnArray
        if (methodCode == 15):
            for html in htmlArray:
                returnArray.append(PlayerStatTools.getRecentSeasonEFTP(html))
            return returnArray
        if (methodCode == 16):
            for html in htmlArray:
                returnArray.append(PlayerStatTools.getCareerEFTP(html))
            return returnArray
