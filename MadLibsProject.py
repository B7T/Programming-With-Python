sInitialPrompt = '\nPress ENTER to begin.'
sNames = '\nEnter the names of 2 people, separated by a comma and space: '
sCity = 'Enter the name of a city: '
sPlaces = 'Enter the names of 2 places, separated by a comma and space: '
sJob = 'Enter a job title: '
sNouns = 'Enter 2 nouns, separated by a comma and space: '
sOccur = 'Enter an occurence: '
sPNouns = 'Enter 2 plural nouns separated by a comma and space: '
sTime = 'Enter a time: '
sUnit = 'Enter a unit of time: '
sSound = 'Enter a sound: '
sAdjs = 'Enter 3 adjectives, separated by two comma/space combinations: '
sAdv = 'Enter an adverb: '
sPrVerb1 = 'Enter a present-tense verb that does not have the -ing suffix: '
sPrVerb2 = 'Enter a present-tense verb with the -ing suffix: '
sPaVerb= 'Enter a singular past-tense verb: '
sIng = 'ing.'
sPeriod = '.'

print('Welcome to My Mad Libs Project!'
    '\nFollow the instructions below to enter the words required for the Mad Libs.'
    '\nPress ENTER to move on to the next step. Hope you enjoy!')

sNameSplit: list = input(sNames).split(', ',2)
sCityInput = input(sCity)
sPlaceSplit: list = input(sPlaces).split(', ',2)
sJobInput = input(sJob)
sNounSplit: list = input(sNouns).split(', ',2)
sOccurInput = input(sOccur)
sPNounSplit: list = input(sPNouns).split(', ',2)
sTimeInput = input(sTime)
sUnitInput = input(sUnit)
sSoundInput = input(sSound)
sAdjSplit: list = input(sAdjs).split(', ',3)
sAdvInput = input(sAdv)
sPrVerb1Input = input(sPrVerb1)
sPrVerb2Input = input(sPrVerb2)
sPaVerbInput = input(sPaVerb)

print('\nOne day, {}'.format(sNameSplit[0]),'went to the {}'.format(sPlaceSplit[0]),'.'
'\nIt was quite {}'.format(sAdjSplit[0]),'to watch how this turned out,'
'\nas he/she decided to {}'.format(sPrVerb1Input),'on the spot.'
'\nAfter this, a(n) {}'.format(sJobInput),'{}'.format(sAdvInput),'{}'.format(sPaVerbInput),
'to them.\n{}'.format(sNameSplit[1]),'saw it coming from a mile away.'
'\nOnce the {}'.format(sOccurInput),'was over, the duo of {}'.format(sNameSplit[0]),
'and {}'.format(sNameSplit[1]),'headed over to {}{}'.format(sCityInput, sPeriod),
'\nThey woke everyone up from their {}'.format(sAdjSplit[1]),'naps with their'
'\n{}'.format(sPNounSplit[0]),'and {}'.format(sAdjSplit[2]),'{}{}'.format(sSoundInput, sIng),
'\nThe city’s {}'.format(sPNounSplit[1]),'all rallied together at the local {}'.format(sPlaceSplit[1]),
'\nand flexed on every {}'.format(sNounSplit[0]),'that they could find.'
'\nIt was over at {}'.format(sTimeInput),'in the afternoon, one {}'.format(sUnitInput),'later.'
'\nEveryone returned to where they were prior to the rally;'
'\napart from the {}'.format(sNounSplit[1]),'cult. They can be found {}'.format(sPrVerb2Input),'to this day.')