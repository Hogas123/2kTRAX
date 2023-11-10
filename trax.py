import pygame, sys

class GamePlayer:
    def __init__(self, n):
        self.name = n

        self.wins = 0
        self.losses = 0
        self.fg = 0
        self.tp = 0

    def get_fgp(self): 
        fg = '{fg:.3f}'
        return fg.format( fg = (self.fg / (self.wins + self.losses)) / 100)
    def get_tpp(self): 
        tp = '{tp:.3f}'
        return tp.format(tp = (self.tp / (self.wins + self.losses)) / 100)
    def toLabelData(self): return [self.fName + " " + self.lName, self.wins, self.losses, self.fg, self.tp]

class NbaTeam:
    def __init__(self, c, n):
        self.city = c
        self.name = n

        self.wins = 0
        self.losses = 0
        self.fg = 0
        self.tp = 0

        self.starsList = []
    def toLabelData(self): return [self.fName + " " + self.lName, self.wins, self.losses, self.fg, self.tp]

    def get_fgp(self): 
        fg = '{fg:.3f}'
        return fg.format( fg = (self.fg / (self.wins + self.losses)) / 100)
    def get_tpp(self): 
        tp = '{tp:.3f}'
        return tp.format(tp = (self.tp / (self.wins + self.losses)) / 100)

class starPlayer:
    def __init__(self, fn, ln, p):
        self.fName = fn
        self.lName = ln

        self.fg = 0
        self.tp = 0

        self.pos = p
    

class Game:
    def __init__(self, p1, p2, t1, t2, s1, s2, f1, f2, tp1, tp2):
        self.player1 = p1
        self.player2 = p2
        self.team1 = t1
        self.team2 = t2
        self.score1 = s1
        self.score2 = s2
        self.fgoal1 = f1
        self.fgoal2 = f2
        self.three1 = tp1
        self.three2 = tp2

    def toText(self): return str(self.player1) + "," + str(self.team1) + "," + str(self.score1) + "," + str(self.fgoal1) + "," + str(self.three1) + "," + str(self.player2) + "," + str(self.team2) + "," + str(self.score2) + "," + str(self.fgoal2) + "," + str(self.three2)
    def toLabelData(self):
        return [self.player1, self.team1, self.score1, self.fgoal1, self.three1, self.player2, self.team2, self.score2, self.fgoal2, self.three2]

class Label:
    def __init__(self,m,w,h,data,type):
        self.width = w
        self.height = h
        self.data = data

        pygame.draw.rect(m.view, "black", (m.width * 0.05, m.height *0.05, self.width, self.height))

        if type == "Game":
            out1 = "Player: " + str(data[0]) + " Team: " + str(data[1]) + " Score: " + str(data[2]) + " FG%: " + str(data[3]) + " 3P%: " + str(data[4]) 
            out2 = "Player: " + str(data[5]) + " Team: " + str(data[6]) + " Score: " + str(data[7]) + " FG%: " + str(data[8]) + " 3P%: " + str(data[9]) 
            text1 = m.displayText.render(out1, 0, "white")
            text2 = m.displayText.render(out2, 0, "white")
            m.view.blit(text1, (20, 100))
            m.view.blit(text2, (20, 130))
            pygame.display.flip()
            
            
        elif type == "Team":
            out1 = "Player: " + str(data[0]) + " RECORD: (" + str(data[1]) + ", " + str(data[2]) + ")" 
            out2 = "AVG Score: " + str(data[3]) + " FG%: " + str(data[4]) + " 3P%: " + str(data[5])
            text1 = m.displayText.render(out1, 0, "white")
            text2 = m.displayText.render(out2, 0, "white")
            m.view.blit(text1, (20, 100))
            m.view.blit(text2, (20, 130))
            pygame.display.flip()
        elif type == "Player":
            out1 = "Team: " + str(data[0]) + " RECORD: (" + str(data[1]) + ", " + str(data[2]) + ")" 
            out2 = "AVG Score: " + str(data[3]) + " FG%: " + str(data[4]) + " 3P%: " + str(data[5])
            text1 = m.displayText.render(out1, 0, "white")
            text2 = m.displayText.render(out2, 0, "white")
            m.view.blit(text1, (20, 100))
            m.view.blit(text2, (20, 130))
            pygame.display.flip()

        pygame.display.flip()

class main:
    def __init__(self):
        self.gameList = []
        self.playerList = []
        self.initNBA()

        pygame.display.init()
        pygame.font.init()
        self.displayText = pygame.font.SysFont("Serif", 28)
        disp_info = pygame.display.Info()
        pygame.display.set_caption("2KTRAX")

        self.view = pygame.display.set_mode((disp_info.current_w / 2.25, disp_info.current_h / 1.35))
        self.width = self.view.get_width()
        self.height = self.view.get_height()

    def setBackground(self):
        baseC = 'dark grey'
        panelC = "light grey"
        
        self.view.fill(baseC)
        self.button_p = pygame.draw.rect(self.view, panelC, (self.width * 0.02, self.height * 0.85, self.width * 0.96, self.height * 0.13 ))
        pygame.display.flip()

    def initNBA(self):

        Bucks = NbaTeam("Millwaukee", "Bucks")
        Bulls = NbaTeam("Chicago", "Bulls")
        Cavaliers = NbaTeam("Cleveland", "Caveliers")
        Celtics = NbaTeam("Boston", "Celtics")
        Clippers = NbaTeam("LA", "Clippers")
        Grizzlies = NbaTeam("Memphis", "Grizzlies")
        Hawks = NbaTeam("Atlanta", "Hawks")
        Heat = NbaTeam("Miami", "Heat")
        Hornets = NbaTeam("Charlotte", "Hornets")
        Jazz = NbaTeam("Utah", "Jazz")
        Kings = NbaTeam("Sacramento", "Kings")
        Knicks = NbaTeam("NY", "Knicks")
        Lakers = NbaTeam("LA", "Lakers")
        Magic = NbaTeam("Orlando", "Magic")
        Mavericks = NbaTeam("Dallas", "Mavericks")
        Nets = NbaTeam("Brooklyn", "Nets")
        Nuggets = NbaTeam("Denver", "Nuggets")
        Pacers = NbaTeam("Indiana", "Pacers")
        Pelicans = NbaTeam("New Orleans", "Pelicans")
        Pistons = NbaTeam("Detroit", "Pistons")
        Raptors = NbaTeam("Toronto", "Raptors")
        Rockets = NbaTeam("Houston", "Rockets")
        Sixers = NbaTeam("Philadelphia", " ")
        Spurs = NbaTeam("San Antonio", "Spurs")
        Suns = NbaTeam("Pheonix", "Suns")
        Thunder = NbaTeam("OKC", "Thunder")
        Timberwolves = NbaTeam("Minnesota", "Timberwolves")
        TBlazers = NbaTeam("Portland", "Trail Blazers")
        Warriors = NbaTeam("Golden State", "Warriors")
        Wizards = NbaTeam("Washington", "Wizards")

        self.teams = [Bucks, Bulls, Cavaliers, Celtics, Clippers, Grizzlies, Hawks, Heat, Hornets, Kings, Knicks, Lakers, Magic, Mavericks, Nets, Nuggets, Pacers, Pelicans, Pistons, Raptors, Rockets, Sixers, Spurs, Suns, Thunder, TBlazers, Timberwolves, Warriors, Wizards]

    def newGame(self):
      #NEED INTERFACE SYSTEM TO BRING IN GAMES PLAYER INTERACTION
        pass

    def save(self):
        f = open("./saveFile.txt", "w")
        f.write("")
        f.close()
        f = open('./saveFile.txt', "a")
        for i in self.gameList:
            f.write(i.toText() + "\n")
        
        f.close()

    def updateStats(self):
        for g in self.gameList:
            if g.player1 not in self.playerList:
                self.playerList.append(GamePlayer(g.player1)) 
            if g.player2 not in self.playerList:
                self.playerList.append(GamePlayer(g.player2))

            x = -1
            for i in self.playerList:
                x+=1
                if i.name == g.player1:
                    break
            p1 = self.playerList[x]
           
            x = -1
            for i in self.playerList:
                x+=1
                if i.name == g.player2:
                    break
            p2 = self.playerList[x]

            x = -1
            for i in self.teams:
                x+=1
                if i.name == g.team1:
                    break

            t1 = self.teams[x]
            x = -1

            for i in self.teams:
                x+=1
                if i.name == g.team2:
                    break

            t2 = self.teams[x]

            if g.score1 > g.score2:
                p1.wins += 1
                p2.losses += 1
                t1.wins += 1
                t2.losses += 1
            else:
                p1.losses += 1
                p2.wins += 1
                t1.losses += 1
                t2.wins += 1

            p1.fg += g.fgoal1
            p2.fg += g.fgoal2
            t1.fg += g.fgoal1
            t2.fg += g.fgoal2
            p1.tp += g.three1
            p2.tp += g.three2
            t1.tp += g.three1
            t2.tp += g.three2


            
    def load(self):
        f = open("./saveFile.txt", "r")
        data = f.readlines()
        if data != ['\n']:
            for g in data:
                g = g.replace('\n', "")
                g_d = g.split(',')
                self.gameList.append(Game(g_d[0], g_d[5], g_d[1], g_d[6], int(g_d[2]), int(g_d[7]), int(g_d[3]), int(g_d[8]), int(g_d[4]), int(g_d[9])))
            self.updateStats()


m = main()
m.load()
m.setBackground()

l = Label(m, 10, 10, [1,2,3,4,5,6,7,8,9,10], "Game" )

running = True

while running:
    for event in pygame.event.get():



        # QUIT app
        if event.type == pygame.QUIT:
            running = False




 

