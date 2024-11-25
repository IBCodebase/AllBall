#rings, plus minus, mvps, all mba, vorp
import time

from bs4 import BeautifulSoup
import requests

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
    html = findPage(playerName)
    return statsPulloutExtractorSeason("Games", html)

def getRecentSeasonGamesHtml(html):
    return statsPulloutExtractorSeason("Games", html)

def getCareerGames(playerName):
    html = findPage(playerName)
    return statsPulloutExtractorCareer("Games", html)

def getCareerGames(html):
    return statsPulloutExtractorCareer("Games", html)

def getRecentSeasonPoints(playerName):
    html = findPage(playerName)
    return statsPulloutExtractorSeason("Points", html)

def getRecentSeasonPointsHtml(html):
    return statsPulloutExtractorSeason("Points", html)

def getCareerPoints(playerName):
    html = findPage(playerName)
    return statsPulloutExtractorCareer("Points", html)

def getCareerPointsHtml(html):
    return statsPulloutExtractorCareer("Points", html)

def getRecentSeasonTotalRebounds(playerName):
    html = findPage(playerName)
    return statsPulloutExtractorSeason("Total Rebounds", html)

def getRecentSeasonTotalReboundsHtml(html):
    return statsPulloutExtractorSeason("Total Rebounds", html)

def getCareerTotalRebounds(playerName):
    html = findPage(playerName)
    return statsPulloutExtractorCareer("Total Rebounds", html)

def getCareerTotalReboundsHtml(html):
    return statsPulloutExtractorCareer("Total Rebounds", html)

def getRecentSeasonAssists(playerName):
    html = findPage(playerName)
    return statsPulloutExtractorSeason("Assists", html)

def getRecentSeasonAssistsHtml(html):
    return statsPulloutExtractorSeason("Assists", html)

def getCareerAssists(playerName):
    html = findPage(playerName)
    return statsPulloutExtractorCareer("Assists", html)

def getCareerAssistsHtml(html):
    return statsPulloutExtractorCareer("Assists", html)

def getRecentSeasonFGP(playerName):
    html = findPage(playerName)
    return statsPulloutExtractorSeason("Field Goal Percentage", html)

def getRecentSeasonFGPHtml(html):
    return statsPulloutExtractorSeason("Field Goal Percentage", html)

def getCareerFGP(playerName):
    html = findPage(playerName)
    return statsPulloutExtractorCareer("Field Goal Percentage", html)

def getCareerFGPHtml(html):
    return statsPulloutExtractorCareer(html)

def getRecentSeason3PointFGP(playerName):
    html = findPage(playerName)
    return statsPulloutExtractorSeason("3-Point Field Goal Percentage", html)

def getRecentSeason3PointFGPHtml(html):
    return statsPulloutExtractorSeason("3-Point Field Goal Percentage", html)

def getCareer3PointFGP(playerName):
    html = findPage(playerName)
    return statsPulloutExtractorCareer("3-Point Field Goal Percentage", html)

def getCareer3PointFGPHtml(html):
    return statsPulloutExtractorCareer("3-Point Field Goal Percentage", html)

def getRecentSeasonFTP(playerName):
    html = findPage(playerName)
    return statsPulloutExtractorSeason("Free Throw Percentage", html)

def getRecentSeasonFTPHtml(html):
    return statsPulloutExtractorSeason("Free Throw Percentage", html)

def getCareerFTP(playerName):
    html = findPage(playerName)
    return statsPulloutExtractorCareer("Free Throw Percentage", html)

def getCareerFTPHtml(html):
    return statsPulloutExtractorCareer("Free Throw Percentage", html)

def getRecentSeasonEFTP(playerName):
    # weird input for extractor because the html coder was inconsistent on web page
    # i.e. blame them
    html = findPage(playerName)
    return statsPulloutExtractorSeason("<strong>Effective Field Goal Percentage", html)

def getRecentSeasonEFTPHtml(html):
    # weird input for extractor because the html coder was inconsistent on web page
    # i.e. blame them
    return statsPulloutExtractorSeason("<strong>Effective Field Goal Percentage", html)

def getCareerEFTP(playerName):
    # weird input for extractor because the html coder was inconsistent on web page
    # i.e. blame them
    html = findPage(playerName)
    return statsPulloutExtractorCareer("<strong>Effective Field Goal Percentage", html)

def getCareerEFTPHtml(html):
    #weird input for extractor because the html coder was inconsistent on web page
    #i.e. blame them
    return statsPulloutExtractorCareer("<strong>Effective Field Goal Percentage", html)

def applyMethodToGroup(methodCode, playerArray, waitTime):
    #recomended waitTime (time in between requests) for this method is 6 second (website limits to 10 requests per

    #This method uses codes to indicate what method you would like to run on a list of
    #players, the codes go as follows
    #1 = getRecentSeasonGames
    #2 = getCareerGames

    if(methodCode == 1):
        returnArray = []
        for player in playerArray:
            returnArray.append(getRecentSeasonGames(player))
            time.sleep(waitTime)
        return returnArray
    if (methodCode == 2):
        returnArray = []
        for player in playerArray:
            returnArray.append(getCareerGames(player))
            time.sleep(waitTime)
        return returnArray




if __name__ == '__main__':
    roster = ["Draymond Green", "Lebron James", "Bronny James", "Josh Hart"]
    print(getCareerEFTP("Draymond Green"))
    print(getRecentSeasonFTP("Draymond Green"))

