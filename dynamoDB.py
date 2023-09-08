"""
import boto3
from botocore.exceptions import ClientError
from pprint import pprint
from decimal import Decimal
import time


client = boto3.client('dynamodb')

#Create DynamoDB table
def create_movie_table():
    table = client.create_table(
        TableName='Movies',
        KeySchema=[
            {
                'AttributeName': 'year',
                'KeyType': 'HASH'  # Partition key
            },
            {
                'AttributeName': 'title',
                'KeyType': 'RANGE'  # Sort key
            }
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'year',
                'AttributeType': 'N'
            },
            {
                'AttributeName': 'title',
                'AttributeType': 'S'
            },

        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )
    return table
"""
#
"""
class vehicle:
    color = 127
    def drivr(self):
        print("on drive")
class car(vehicle):
    fule = 890
    def owner(self):
        print("off drive")
c1=car()
c1.drivr()              #on drive
c1.owner()              #off drive
v1 = vehicle()
v1.drivr()              #on drive
v1.owner()
"""




#Fluentlife:-1)coffin Dancers,2)Japan's Batman,3)Child Prodigy
#1)Ghana's Dancing Pallbearers:-for mourners wanting a more upbeat=marintha ulasanga undalanukune duhkgitula kosam
#Mourners synonyms=Pallbearer,griever,sorrower,weeper, and bemoaner(Dhukinchuta). 
#coffin=pade,shava petiki.

#2)Sophia tran Thomson is reporting:-(Japan's batman)He is a chi batman of chiba over the past 3 years. he travels with his 3wheeled chi batpod & he became an internet superhero one of his video got viral on social media.The motivation behind the mask is honorable.after the earth quick and fukushima power plant disaster broken japan in 2011.due to earth quake they forgot how to smile so that he decided to bring back smile on there faces. it is unusal idea works.he is a unique. He is a 41 year old welder with a penchant leather and masks he also some times dresses up a star wars stormtrooper. but he always remember their fav hero chi batman forever. sofia tran thompson BBC news. 
#sightings=analysis,detection,diagnosis,disclosure.     devastated=brken,lostravaged,ruined,smashed.     embarrassed=feels shy,ashmed,or guilty about something.  


#3)she was playing piano from the age 2 and violan was from age 3.she started compose from age 4 she written down on a paper she desn't even know that is called as composing. she came at the age 9 to play henley festival tomorrow and what are playing. she says loyly to watch she listening the music and asking how would you feel when listening that.when she was playing the orchestra inthe beginning she thought that they were a littile bit suspicious and they looked whos this littile girl.she turned to them and start she  take her cadenza they changed their minds immediatley.that she says when youre sompose while skipping yes she says i can do she have an escape in rope which actually she dont skip with it.she just wave it round and she tell stories in her head and then sometimes a melody just pops into her her head by that she get her tunes. waking up and falling sleep or watching the middle of night when iam asleep but getting the tunes actually thats easy but then having to sit sown and develop it into proper pieces and combining with a melodies in a coherant way that is difficult bit for her. you like Mozart and how would you fell about that well. Mozart it is little bit boring she worried exactly what mozart had written before she prefer little Alma  

#upbeat:cheerful,positive,hopeful,confident
#pallbearers:griever,lamenter,mourner,sorrower(carrying the coffin at a funeral)
#solmen:earnest,grave,sedate,serious,staid

#Orchard - An orchard is an intentional plantation of trees or shrubs that is maintained for food production.
#Grove -  a small group of trees, especially of one particular type
#Abundant - present in great quantity
#Circus - a show performed in a large tent by a company of people and animals
#Entertainment - Entertainment is a form of activity that holds the attention and interest of an audience or gives pleasure and delight. 
#Acrobatics - involving a lot of skill and energy in controlling the movement of your body to do something difficult
#Monument - an old building or other place that is of historical importance
#Mughal - a member of the Muslim dynasty of Indian emperors established by the Mughal Emperor Babur
#Mausoleum - a stately or impressive building housing a tomb or group of tombs.

#augment:increase,add to,supplement,build up,enlarge,expand
#emerge:comeout,appear,turn up,arise
#endorsements:support,backing,approval,agreement,advocacy

#nomad:migrant,pilgrim,vagabond,wanderer.
#meticulously:careful,pumctilious,scrupulous
#pomp:ceremony,ritual,display,spectacle
#diaspora:resetting,moving,emigration,posting

#swagger:bluster,prance,boast,strut
#sensation:viral,uproar,impact,interest,stir
#ghetto:slum,public squalor,tenement
#demographics:popular,representative,populist

#impression:feeling,sense,fancy,idea,notion,opinion,perception
#embarrass:confuse,fluster,bother,distrub,humiliate
#boarded:geton,enter,climb on,mount,ascend.
#heels:madly,
#meadow:field,pasture,grassland
#dramatize:overplay,overdo,overstress,amplify,expand on
#majestic:great,awesome,stately,diginified,solemn,magnificent
#hitchhike:the person who takes lift to travel from one place to another place.
#drove:operate,pilot,steer,handle,manage
#treacherous:not trusted or dengerous,uneven surface
#Rohtang pass:pile of dead bodies
#worth:apprecite,cherish,prize,treasure,collectible,expensive,incalculable,invaluable. 
#apparent:clear,distinct,evident,manifest,obvious,patent.
#rejuvenate:restore,revive,refresh,recreate,renew,renovate.

#Altar(shrine,font):An altar is a structure upon which offerings are made for religious purposes. Altars are found at shrines, temples, churches and other places of worship.
#Aisle(passage) - a passage between the rows of seats in a church, theatre, etc.
#Nuptials(marriage,martial,conjugal) - a wedding
#Concert - a live music performance in front of an audience.
#Jam-packed - extremely crowded or full to capacity.
#Unison - the playing or singing of notes at the same pitch by different instruments or voices.
#Playground - an area of land where children can play
#Childhood - The time were you were a child 
#Innocence - lack of knowledge and experience of the world, especially of bad things

#Activist:fights for some change
#Apartheid:separate,segregated,discimination,racism,
#global Advocate:acclaimed world wide. advocate fight for justice
#Repressive:controlling people by force
#Regime:rule,method,pattern
#Eradication:abolish,renmoval
#Transition:change
#Ethnic:connection with history,traditional
#Inspiration:Motivated,influenced,follow