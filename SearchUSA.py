import sys
import math

searchCriteria = sys.argv[1]
start = sys.argv[2]
end = sys.argv[3]
pi = 3.14

lat_long = {
    'albanyGA': (31.58, 84.17),
    'albanyNY': (42.66, 73.78),
    'albuquerque': (35.11, 106.61),
    'atlanta': (33.76, 84.40),
    'augusta': (33.43, 82.02),
    'austin': (30.30, 97.75),
    'bakersfield': (35.36, 119.03),
    'baltimore': (39.31, 76.62),
    'batonRouge': (30.46, 91.14),
    'beaumont': (30.08, 94.13),
    'boise': (43.61, 116.24),
    'boston': (42.32, 71.09),
    'buffalo': (42.90, 78.85),
    'calgary': (51.00, 114.00),
    'charlotte': (35.21, 80.83),
    'chattanooga': (35.05, 85.27),
    'chicago': (41.84, 87.68),
    'cincinnati': (39.14, 84.50),
    'cleveland': (41.48, 81.67),
    'coloradoSprings': (38.86, 104.79),
    'columbus': (39.99, 82.99),
    'dallas': (32.80, 96.79),
    'dayton': (39.76, 84.20),
    'daytonaBeach': (29.21, 81.04),
    'denver': (39.73, 104.97),
    'desMoines': (41.59, 93.62),
    'elPaso': (31.79, 106.42),
    'eugene': (44.06, 123.11),
    'europe': (48.87, -2.33),
    'ftWorth': (32.74, 97.33),
    'fresno': (36.78, 119.79),
    'grandJunction': (39.08, 108.56),
    'greenBay': (44.51, 88.02),
    'greensboro': (36.08, 79.82),
    'houston': (29.76, 95.38),
    'indianapolis': (39.79, 86.15),
    'jacksonville': (30.32, 81.66),
    'japan': (35.68, 220.23),
    'kansasCity': (39.08, 94.56),
    'keyWest': (24.56, 81.78),
    'lafayette': (30.21, 92.03),
    'lakeCity': (30.19, 82.64),
    'laredo': (27.52, 99.49),
    'lasVegas': (36.19, 115.22),
    'lincoln': (40.81, 96.68),
    'littleRock': (34.74, 92.33),
    'losAngeles': (34.03, 118.17),
    'macon': (32.83, 83.65),
    'medford': (42.33, 122.86),
    'memphis': (35.12, 89.97),
    'mexia': (31.68, 96.48),
    'mexico': (19.40, 99.12),
    'miami': (25.79, 80.22),
    'midland': (43.62, 84.23),
    'milwaukee': (43.05, 87.96),
    'minneapolis': (44.96, 93.27),
    'modesto': (37.66, 120.99),
    'montreal': (45.50, 73.67),
    'nashville': (36.15, 86.76),
    'newHaven': (41.31, 72.92),
    'newOrleans': (29.97, 90.06),
    'newYork': (40.70, 73.92),
    'norfolk': (36.89, 76.26),
    'oakland': (37.80, 122.23),
    'oklahomaCity': (35.48, 97.53),
    'omaha': (41.26, 96.01),
    'orlando': (28.53, 81.38),
    'ottawa': (45.42, 75.69),
    'pensacola': (30.44, 87.21),
    'philadelphia': (40.72, 76.12),
    'phoenix': (33.53, 112.08),
    'pittsburgh': (40.40, 79.84),
    'pointReyes': (38.07, 122.81),
    'portland': (45.52, 122.64),
    'providence': (41.80, 71.36),
    'provo': (40.24, 111.66),
    'raleigh': (35.82, 78.64),
    'redding': (40.58, 122.37),
    'reno': (39.53, 119.82),
    'richmond': (37.54, 77.46),
    'rochester': (43.17, 77.61),
    'sacramento': (38.56, 121.47),
    'salem': (44.93, 123.03),
    'salinas': (36.68, 121.64),
    'saltLakeCity': (40.75, 111.89),
    'sanAntonio': (29.45, 98.51),
    'sanDiego': (32.78, 117.15),
    'sanFrancisco': (37.76, 122.44),
    'sanJose': (37.30, 121.87),
    'sanLuisObispo': (35.27, 120.66),
    'santaFe': (35.67, 105.96),
    'saultSteMarie': (46.49, 84.35),
    'savannah': (32.05, 81.10),
    'seattle': (47.63, 122.33),
    'stLouis': (38.63, 90.24),
    'stamford': (41.07, 73.54),
    'stockton': (37.98, 121.30),
    'tallahassee': (30.45, 84.27),
    'tampa': (27.97, 82.46),
    'thunderBay': (48.38, 89.25),
    'toledo': (41.67, 83.58),
    'toronto': (43.65, 79.38),
    'tucson': (32.21, 110.92),
    'tulsa': (36.13, 95.94),
    'uk1': (51.30, 0.00),
    'uk2': (51.30, 0.00),
    'vancouver': (49.25, 123.10),
    'washington': (38.91, 77.01),
    'westPalmBeach': (26.71, 80.05),
    'wichita': (37.69, 97.34),
    'winnipeg': (49.90, 97.13),
    'yuma': (32.69, 114.62)
}

class Search(object):
    def __init__(self):
        self.frontiers = {}
        self.explored = []
        self.hierarchy = {}

    def getCoordinates(self, place):
        return lat_long[place]

    def get_heuristic_value(self, city, destination):
        co_ordinates1 = list(self.getCoordinates(city))
        co_ordinates2 = list(self.getCoordinates(destination))
        return math.sqrt((69.5 * (co_ordinates1[0] - co_ordinates2[0])) ** 2 + (69.5 * math.cos((co_ordinates1[0] + co_ordinates2[0])/360 * pi) * (co_ordinates1[1] - co_ordinates2[1])) ** 2)

    def getStartToNodeCost(self, node):
        parent, cost = self.hierarchy[node]
        while node != parent:
            node = parent
            parent, connectingCost = self.hierarchy[node]
            cost += connectingCost
        return cost

    def generateOutput(self, dest):
        totalCost = self.getStartToNodeCost(dest)
        parent, cost = self.hierarchy[dest]
        resultantPath = [dest]
        while dest != parent:
            resultantPath.append(parent)
            dest = parent
            parent, _ = self.hierarchy[dest]
        print('Explored/Expanded Nodes:: \n{}\n'.format(self.explored))
        print('Explored/Expanded Nodes Count:: {}\n'.format(len(self.explored)))
        resultantPath.reverse()
        print('Solution Path:: \n{}\n'.format(resultantPath))
        print('Total Number of Nodes in Solution Path:: {}\n'.format(len(resultantPath)))
        print('Cost of Solution Path:: {}'.format(totalCost))

    def getChildren(self, node):
        children = []
        for road in Roads:
            if(road[0] == node):
                children.append((road[1], road[2]))
        return children

    def pop(self):
        minVal = min(self.frontiers.values())
        for city, cost in self.frontiers.items():
            if (minVal == cost):
                self.frontiers.pop(city)
                return city

    def update(self, children, nextItem, frm, to, criteria):
        for child, cost in children:
            heuristicValue = self.get_heuristic_value(child, to)
            if criteria == 'greedy':
                totalCost = heuristicValue
            elif searchCriteria == 'dynamic':
                totalCost = cost + self.getStartToNodeCost(nextItem)
            elif searchCriteria == 'astar':
                totalCost = cost + \
                    self.getStartToNodeCost(nextItem) + heuristicValue
            else:
                print("Invalid Search Criteria Passed")
            if child in self.explored:
                continue
            if child not in self.frontiers:
                self.frontiers[child] = totalCost
                self.hierarchy[child] = (nextItem, cost)
            elif child in self.frontiers and self.frontiers[child] > totalCost:
                self.hierarchy[child] = (nextItem, cost)
                self.frontiers[child] = totalCost
            else:
                pass

    def computeRoute(self, criteria, frm, to):
        self.frontiers[frm] = 0 + self.get_heuristic_value(frm, to)
        self.hierarchy[frm] = (frm, 0)
        while self.frontiers:
            nextItem = self.pop()
            if(nextItem == to):
                self.generateOutput(nextItem)
                return
            else:
                self.explored.append(nextItem)
                self.update(self.getChildren(nextItem),
                            nextItem, frm, to, criteria)
        print("Failure")

Roads = [
    ('albanyNY', 'montreal', 226),
    ('albanyNY', 'boston', 166),
    ('albanyNY', 'rochester', 148),
    ('albanyGA', 'tallahassee', 120),
    ('albanyGA', 'macon', 106),
    ('albuquerque', 'elPaso', 267),
    ('albuquerque', 'santaFe', 61),
    ('atlanta', 'macon', 82),
    ('atlanta', 'chattanooga', 117),
    ('augusta', 'charlotte', 161),
    ('augusta', 'savannah', 131),
    ('austin', 'houston', 186),
    ('austin', 'sanAntonio', 79),
    ('bakersfield', 'losAngeles', 112),
    ('bakersfield', 'fresno', 107),
    ('baltimore', 'philadelphia', 102),
    ('baltimore', 'washington', 45),
    ('batonRouge', 'lafayette', 50),
    ('batonRouge', 'newOrleans', 80),
    ('beaumont', 'houston', 69),
    ('beaumont', 'lafayette', 122),
    ('boise', 'saltLakeCity', 349),
    ('boise', 'portland', 428),
    ('boston', 'providence', 51),
    ('buffalo', 'toronto', 105),
    ('buffalo', 'rochester', 64),
    ('buffalo', 'cleveland', 191),
    ('calgary', 'vancouver', 605),
    ('calgary', 'winnipeg', 829),
    ('charlotte', 'greensboro', 91),
    ('chattanooga', 'nashville', 129),
    ('chicago', 'milwaukee', 90),
    ('chicago', 'midland', 279),
    ('cincinnati', 'indianapolis', 110),
    ('cincinnati', 'dayton', 56),
    ('cleveland', 'pittsburgh', 157),
    ('cleveland', 'columbus', 142),
    ('coloradoSprings', 'denver', 70),
    ('coloradoSprings', 'santaFe', 316),
    ('columbus', 'dayton', 72),
    ('dallas', 'denver', 792),
    ('dallas', 'mexia', 83),
    ('daytonaBeach', 'jacksonville', 92),
    ('daytonaBeach', 'orlando', 54),
    ('denver', 'wichita', 523),
    ('denver', 'grandJunction', 246),
    ('desMoines', 'omaha', 135),
    ('desMoines', 'minneapolis', 246),
    ('elPaso', 'sanAntonio', 580),
    ('elPaso', 'tucson', 320),
    ('eugene', 'salem', 63),
    ('eugene', 'medford', 165),
    ('europe', 'philadelphia', 3939),
    ('ftWorth', 'oklahomaCity', 209),
    ('fresno', 'modesto', 109),
    ('grandJunction', 'provo', 220),
    ('greenBay', 'minneapolis', 304),
    ('greenBay', 'milwaukee', 117),
    ('greensboro', 'raleigh', 74),
    ('houston', 'mexia', 165),
    ('indianapolis', 'stLouis', 246),
    ('jacksonville', 'savannah', 140),
    ('jacksonville', 'lakeCity', 113),
    ('japan', 'pointReyes', 5131),
    ('japan', 'sanLuisObispo', 5451),
    ('kansasCity', 'tulsa', 249),
    ('kansasCity', 'stLouis', 256),
    ('kansasCity', 'wichita', 190),
    ('keyWest', 'tampa', 446),
    ('lakeCity', 'tampa', 169),
    ('lakeCity', 'tallahassee', 104),
    ('laredo', 'sanAntonio', 154),
    ('laredo', 'mexico', 741),
    ('lasVegas', 'losAngeles', 275),
    ('lasVegas', 'saltLakeCity', 486),
    ('lincoln', 'wichita', 277),
    ('lincoln', 'omaha', 58),
    ('littleRock', 'memphis', 137),
    ('littleRock', 'tulsa', 276),
    ('losAngeles', 'sanDiego', 124),
    ('losAngeles', 'sanLuisObispo', 182),
    ('medford', 'redding', 150),
    ('memphis', 'nashville', 210),
    ('miami', 'westPalmBeach', 67),
    ('midland', 'toledo', 82),
    ('minneapolis', 'winnipeg', 463),
    ('modesto', 'stockton', 29),
    ('montreal', 'ottawa', 132),
    ('newHaven', 'providence', 110),
    ('newHaven', 'stamford', 92),
    ('newOrleans', 'pensacola', 268),
    ('newYork', 'philadelphia', 101),
    ('norfolk', 'richmond', 92),
    ('norfolk', 'raleigh', 174),
    ('oakland', 'sanFrancisco', 8),
    ('oakland', 'sanJose', 42),
    ('oklahomaCity', 'tulsa', 105),
    ('orlando', 'westPalmBeach', 168),
    ('orlando', 'tampa', 84),
    ('ottawa', 'toronto', 269),
    ('pensacola', 'tallahassee', 120),
    ('philadelphia', 'pittsburgh', 319),
    ('philadelphia', 'newYork', 101),
    ('philadelphia', 'uk1', 3548),
    ('philadelphia', 'uk2', 3548),
    ('phoenix', 'tucson', 117),
    ('phoenix', 'yuma', 178),
    ('pointReyes', 'redding', 215),
    ('pointReyes', 'sacramento', 115),
    ('portland', 'seattle', 174),
    ('portland', 'salem', 47),
    ('reno', 'saltLakeCity', 520),
    ('reno', 'sacramento', 133),
    ('richmond', 'washington', 105),
    ('sacramento', 'sanFrancisco', 95),
    ('sacramento', 'stockton', 51),
    ('salinas', 'sanJose', 31),
    ('salinas', 'sanLuisObispo', 137),
    ('sanDiego', 'yuma', 172),
    ('saultSteMarie', 'thunderBay', 442),
    ('saultSteMarie', 'toronto', 436),
    ('seattle', 'vancouver', 115),
    ('thunderBay', 'winnipeg', 440),
    ('montreal', 'albanyNY', 226),
    ('boston', 'albanyNY', 166),
    ('rochester', 'albanyNY', 148),
    ('tallahassee', 'albanyGA', 120),
    ('macon', 'albanyGA', 106),
    ('elPaso', 'albuquerque', 267),
    ('santaFe', 'albuquerque', 61),
    ('macon', 'atlanta', 82),
    ('chattanooga', 'atlanta', 117),
    ('charlotte', 'augusta', 161),
    ('savannah', 'augusta', 131),
    ('houston', 'austin', 186),
    ('sanAntonio', 'austin', 79),
    ('losAngeles', 'bakersfield', 112),
    ('fresno', 'bakersfield', 107),
    ('philadelphia', 'baltimore', 102),
    ('washington', 'baltimore', 45),
    ('lafayette', 'batonRouge', 50),
    ('newOrleans', 'batonRouge', 80),
    ('houston', 'beaumont', 69),
    ('lafayette', 'beaumont', 122),
    ('saltLakeCity', 'boise', 349),
    ('portland', 'boise', 428),
    ('providence', 'boston', 51),
    ('toronto', 'buffalo', 105),
    ('rochester', 'buffalo', 64),
    ('cleveland', 'buffalo', 191),
    ('vancouver', 'calgary', 605),
    ('winnipeg', 'calgary', 829),
    ('greensboro', 'charlotte', 91),
    ('nashville', 'chattanooga', 129),
    ('milwaukee', 'chicago', 90),
    ('midland', 'chicago', 279),
    ('indianapolis', 'cincinnati', 110),
    ('dayton', 'cincinnati', 56),
    ('pittsburgh', 'cleveland', 157),
    ('columbus', 'cleveland', 142),
    ('denver', 'coloradoSprings', 70),
    ('santaFe', 'coloradoSprings', 316),
    ('dayton', 'columbus', 72),
    ('denver', 'dallas', 792),
    ('mexia', 'dallas', 83),
    ('jacksonville', 'daytonaBeach', 92),
    ('orlando', 'daytonaBeach', 54),
    ('wichita', 'denver', 523),
    ('grandJunction', 'denver', 246),
    ('omaha', 'desMoines', 135),
    ('minneapolis', 'desMoines', 246),
    ('sanAntonio', 'elPaso', 580),
    ('tucson', 'elPaso', 320),
    ('salem', 'eugene', 63),
    ('medford', 'eugene', 165),
    ('philadelphia', 'europe', 3939),
    ('oklahomaCity', 'ftWorth', 209),
    ('modesto', 'fresno', 109),
    ('provo', 'grandJunction', 220),
    ('minneapolis', 'greenBay', 304),
    ('milwaukee', 'greenBay', 117),
    ('raleigh', 'greensboro', 74),
    ('mexia', 'houston', 165),
    ('stLouis', 'indianapolis', 246),
    ('savannah', 'jacksonville', 140),
    ('lakeCity', 'jacksonville', 113),
    ('pointReyes', 'japan', 5131),
    ('sanLuisObispo', 'japan', 5451),
    ('tulsa', 'kansasCity', 249),
    ('stLouis', 'kansasCity', 256),
    ('wichita', 'kansasCity', 190),
    ('tampa', 'keyWest', 446),
    ('tampa', 'lakeCity', 169),
    ('tallahassee', 'lakeCity', 104),
    ('sanAntonio', 'laredo', 154),
    ('mexico', 'laredo', 741),
    ('losAngeles', 'lasVegas', 275),
    ('saltLakeCity', 'lasVegas', 486),
    ('wichita', 'lincoln', 277),
    ('omaha', 'lincoln', 58),
    ('memphis', 'littleRock', 137),
    ('tulsa', 'littleRock', 276),
    ('sanDiego', 'losAngeles', 124),
    ('sanLuisObispo', 'losAngeles', 182),
    ('redding', 'medford', 150),
    ('nashville', 'memphis', 210),
    ('westPalmBeach', 'miami', 67),
    ('toledo', 'midland', 82),
    ('winnipeg', 'minneapolis', 463),
    ('stockton', 'modesto', 29),
    ('ottawa', 'montreal', 132),
    ('providence', 'newHaven', 110),
    ('stamford', 'newHaven', 92),
    ('pensacola', 'newOrleans', 268),
    ('philadelphia', 'newYork', 101),
    ('richmond', 'norfolk', 92),
    ('raleigh', 'norfolk', 174),
    ('sanFrancisco', 'oakland', 8),
    ('sanJose', 'oakland', 42),
    ('tulsa', 'oklahomaCity', 105),
    ('westPalmBeach', 'orlando', 168),
    ('tampa', 'orlando', 84),
    ('toronto', 'ottawa', 269),
    ('tallahassee', 'pensacola', 120),
    ('pittsburgh', 'philadelphia', 319),
    ('newYork', 'philadelphia', 101),
    ('uk1', 'philadelphia', 3548),
    ('uk2', 'philadelphia', 3548),
    ('tucson', 'phoenix', 117),
    ('yuma', 'phoenix', 178),
    ('redding', 'pointReyes', 215),
    ('sacramento', 'pointReyes', 115),
    ('seattle', 'portland', 174),
    ('salem', 'portland', 47),
    ('saltLakeCity', 'reno', 520),
    ('sacramento', 'reno', 133),
    ('washington', 'richmond', 105),
    ('sanFrancisco', 'sacramento', 95),
    ('stockton', 'sacramento', 51),
    ('sanJose', 'salinas', 31),
    ('sanLuisObispo', 'salinas', 137),
    ('yuma', 'sanDiego', 172),
    ('thunderBay', 'saultSteMarie', 442),
    ('toronto', 'saultSteMarie', 436),
    ('vancouver', 'seattle', 115),
    ('winnipeg', 'thunderBay', 440)
]

searchObject = Search()
searchObject.computeRoute(searchCriteria, start, end)
