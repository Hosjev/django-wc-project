from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request, "home.html")


def count(request):
    fulltext = request.GET["fulltext"]
    wordList = fulltext.split()
    wordDict = {}
    for word in wordList:
        if word in wordDict:
            wordDict[word] += 1
        else:
            wordDict[word] = 1

    sortedWords = sorted(wordDict.items(),
                         key=lambda item: item[1],
                         reverse=True)

    return render(request, "count.html", {
        "fulltext": fulltext,
        "count": len(wordList),
        # "words": wordDict,
        # "words": wordDict.items(),
        "words": sortedWords,
    })


def about(request):
    return render(request, "about.html")
