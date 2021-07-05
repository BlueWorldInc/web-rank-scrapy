import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = open("./data/data.csv", "r", encoding="utf-8")
languageArray = ['Scala', 'Go', 'Swift', 'Ruby', 'Kotlin', 'C', 'C#', 'C++', 'Java', 'PHP', 'NodeJS', 'Python 3']
languageArrayPercentage = [0.003727549983056591, 0.0057607590647238225, 0.0057607590647238225, 0.009149440867502542, 0.010504913588614028, 
0.033209081667231445, 0.06675703151474077, 0.06912910877668586, 0.11284310403253135, 0.13859708573364962, 0.1748559810233819, 0.36970518468315827]
totalNumber = 2951

### Graphique 1

def graph1():
    
    langs = []

    for line in data:
        line = line.split(";")
        rank = line[0]
        name = line[1]
        lang = line[2]
        exer = line[3]
        time = line[4]
        orga = line[5]
        langs.append(lang)

    langsArray = np.array(langs)

    unique_elements, counts_elements = np.unique(langsArray, return_counts=True)
    np.asarray((unique_elements, counts_elements))

    langDict = {}

    i = 0
    for lang in unique_elements:
        langDict[lang] = counts_elements[i]
        i += 1

    langDict = {k: v for k, v in sorted(langDict.items(), key=lambda item: item[1])}

    fig, ax = plt.subplots()  # Create a figure containing a single axes.
    # .set_yscale('linear')
    plt.yticks(np.arange(0, max(langDict.values()) + 100, 50))
    p = ax.bar(langDict.keys(), langDict.values())  # Plot some data on the axes.
    ax.bar_label(p)
    plt.show()

### Graphique 2

def graph2(range = 100, percentage = False):

    langs = []

    for line in data:
        line = line.split(";")
        rank = line[0]
        name = line[1]
        lang = line[2]
        exer = line[3]
        time = line[4]
        orga = line[5]
        langs.append(lang)

    langsArray = np.array(langs[0:range])

    unique_elements, counts_elements = np.unique(langsArray, return_counts=True)
    np.asarray((unique_elements, counts_elements))

    langDict = {}

    i = 0
    for lang in unique_elements:
        langDict[lang] = counts_elements[i]
        i += 1

    langDict = {k: v for k, v in sorted(langDict.items(), key=lambda item: item[1])}

    if (percentage):
        for i in langDict:
            langDict[i] = langDict[i] / totalNumber

    fig, ax = plt.subplots()  # Create a figure containing a single axes.
    # .set_yscale('linear')
    plt.yticks(np.arange(0, max(langDict.values()) + 100, 50))
    
    p = ax.bar(langDict.keys(), langDict.values())  # Plot some data on the axes.
    ax.bar_label(p)
    plt.show()

### Graphique 3

def graph3():

    langs = []
    langDict = {}
    for j in range(len(languageArray)):
        langDict[languageArray[j]] = {}
        for i in range(6):
            langDict[languageArray[j]]["Exercice " + str(i+1)] = 0
        langDict[languageArray[j]]["Total"] = 0
        langDict[languageArray[j]]["Average exercice completed"] = 0
        langDict[languageArray[j]]["Average rank achieved"] = 0

    for line in data:
        line = line.split(";")
        rank = line[0]
        name = line[1]
        lang = line[2]
        exer = line[3]
        time = line[4]
        orga = line[5]
        langs.append(lang)
        for j in range(len(languageArray)):
            if (lang == languageArray[j] and int(exer) > 1):
                langDict[languageArray[j]]["Exercice " + exer] += 1
                langDict[languageArray[j]]["Total"] += 1
                langDict[languageArray[j]]["Average rank achieved"] += int(rank)
                break
    
    for j in range(len(languageArray)):
        for i in range(6):
            langDict[languageArray[j]]["Exercice " + str(i+1)] = (langDict[languageArray[j]]["Exercice " + str(i+1)] / langDict[languageArray[j]]["Total"])
            langDict[languageArray[j]]["Average exercice completed"] += langDict[languageArray[j]]["Exercice " + str(i+1)] * (i+1)
            langDict[languageArray[j]]["Exercice " + str(i+1)] = format(langDict[languageArray[j]]["Exercice " + str(i+1)], '.2f')
        langDict[languageArray[j]]["Average rank achieved"] = langDict[languageArray[j]]["Average rank achieved"] / langDict[languageArray[j]]["Total"]

    for l in langDict:
        langDict[l]["Average exercice completed"] = format(langDict[l]["Average exercice completed"], '.2f')
        print(l, ((10-len(l))*" "), langDict[l])

    avgExerciceDict = {}

    for j in  range(0, len(languageArray)):
        avgExerciceDict[languageArray[j]] = float(langDict[languageArray[j]]["Average exercice completed"])


    avgRankDict = {}

    for j in  range(0, len(languageArray)):
        avgRankDict[languageArray[j]] = float(langDict[languageArray[j]]["Average rank achieved"])

    # print(avgRankDict)

    ## Average Exercice Completed

    fig, ax = plt.subplots()  # Create a figure containing a single axes.
    # .set_yscale('linear')
    plt.yticks(np.arange(1, 6, 0.1))
    
    # print(langDict.values())

    p = ax.bar(avgExerciceDict.keys(), avgExerciceDict.values())  # Plot some data on the axes.
    ax.bar_label(p)
    ax.set_ylim(bottom=2)
    plt.show()

    ## Average Rank Achieved

    # fig, ax = plt.subplots()  # Create a figure containing a single axes.
    # # .set_yscale('linear')
    # plt.yticks(np.arange(0, 3000, 100))
    
    # # print(langDict.values())

    # p = ax.bar(avgRankDict.keys(), avgRankDict.values())  # Plot some data on the axes.
    # ax.bar_label(p)
    # ax.set_ylim(bottom=1)
    # plt.show()

def graph4():

    lines = []
    c = 0
    cArray = []

    langDict = {}

    for j in range(len(languageArray)):
        langDict[languageArray[j]] = {}
        langDict[languageArray[j]]["point"] = 0
        langDict[languageArray[j]]["pointArray"] = []
        langDict[languageArray[j]]["pointArrayNormalized"] = []

    for line in data:
        line = line.split(";")
        rank = line[0]
        name = line[1]
        lang = line[2]
        exer = line[3]
        time = line[4]
        orga = line[5]
        lines.append(line)

    for line in reversed(lines):
        rank = line[0]
        name = line[1]
        lang = line[2]
        exer = line[3]
        time = line[4]
        orga = line[5]
        c += 1
        # # print(format(c / totalNumber, '.4f'))
        for j in range(len(languageArray)):
            if (lang == languageArray[j]):
                langDict[languageArray[j]]["point"] += 1
                # if (p >= 25):
                langDict[languageArray[j]]["pointArray"].append((langDict[languageArray[j]]["point"]/c)/languageArrayPercentage[j])
                break

            # print(format(p/c, '.4f'))

    ## Normalize Arrays to 100


    for j in range(len(languageArray)):
        for i in range(100):
            langDict[languageArray[j]]["pointArrayNormalized"].append(langDict[languageArray[j]]["pointArray"][(i * len(langDict[languageArray[j]]["pointArray"])) // 100])


    fig, ax = plt.subplots()  # Create a figure containing a single axes.
    n = 11
    for j in range(n, n+1):
        ax.plot(langDict[languageArray[j]]["pointArrayNormalized"], label=languageArray[j])  # Plot some data on the axes.
    plt.xlim(20)
    plt.legend()
    plt.show()


def graph5():

    lines = []
    c = 0
    skip = 0

    langDict = {}

    for j in range(len(languageArray)):
        langDict[languageArray[j]] = {}
        langDict[languageArray[j]]["point"] = 0
        langDict[languageArray[j]]["pointArray"] = []
        langDict[languageArray[j]]["pointArrayNormalized"] = []

    for line in data:
        line = line.split(";")
        rank = line[0]
        name = line[1]
        lang = line[2]
        exer = line[3]
        time = line[4]
        orga = line[5]
        skip += 1
        if (skip > 2901):
            break
        lines.append(line)

    d = 0

    for line in reversed(lines):
        rank = line[0]
        name = line[1]
        lang = line[2]
        exer = line[3]
        time = line[4]
        orga = line[5]
        c += 1
        # # print(format(c / totalNumber, '.4f'))
        for j in range(len(languageArray)):
            if (lang == languageArray[j]):
                langDict[languageArray[j]]["point"] += 1
                # if (p >= 25):
                # langDict[languageArray[j]]["pointArray"].append((langDict[languageArray[j]]["point"]/c)/languageArrayPercentage[j])
                break

        if (((c-1)%290)==0 and c-1 > 0):
            d += 1
            for j in range(len(languageArray)):
                langDict[languageArray[j]]["pointArray"].append((langDict[languageArray[j]]["point"]/290))
                langDict[languageArray[j]]["point"] = 0



            # print(format(p/c, '.4f'))

    ## Normalize Arrays to 100

    # print(langDict[languageArray[-1]]["pointArray"])

    # for j in range(len(languageArray)):
    #     for i in range(100):
    #         langDict[languageArray[j]]["pointArrayNormalized"].append(langDict[languageArray[j]]["pointArray"][(i * len(langDict[languageArray[j]]["pointArray"])) // 100])


    fig, ax = plt.subplots()  # Create a figure containing a single axes.
    n = 11
    for j in range(5, 12):
        ax.plot(langDict[languageArray[j]]["pointArray"], label=languageArray[j])  # Plot some data on the axes.
    plt.ylim(0)
    plt.legend()
    plt.show()

graph5()