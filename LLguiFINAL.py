# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 14:51:55 2021

@author: J.Michael
"""

import sys
from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtCore import QLine, Qt
from PyQt5.QtWidgets import QButtonGroup, QGridLayout,QMenuBar, QTableWidget,QTableWidgetItem,QScrollArea,QHBoxLayout, QLabel, QMainWindow, QAction, QMessageBox, QPushButton, QRadioButton, QVBoxLayout, qApp, QApplication, QLineEdit, QWidget
#from PyQt5.QtGui import QIcon, QTextBlock
from PyQt5.QtGui import (QPen, QPixmap, QPainter, QColor)
import random



class CardDeck:
    """create the deck of cards for the game. each card has a name, effect, 
    a state of being in the deck or in player hand, and a state of being played
    from players hand. maybe also an associated picture file"""
    def __init__(self, name, effect, dealt_status, played_status):
        self.card_name = name
        self.effect = effect
        self.dealt_status = dealt_status
        self.played_status = played_status
        #self.picture_file = picture
    def getName(self):
        return self.name
    
    
class Player:
    """create the players for the Love Letter Game. each player has a name,
    a hand of cards, a turn status, a protected status via the handmaid, and a number of
    accrued tokens"""
    def __init__(self,name,turn_status,round_status,tokens):
        self.player_name = name
        self.hand = []
        self.is_turn_status = turn_status
        self.protected_status = round_status
        self.tokens = tokens

def make_deck():
    """creates the deck of cards and returns them as a list of CardDeck objects"""
    king = CardDeck('king',7,False,False) #0
    princess = CardDeck('princess',9,False,False) #1
    countess= CardDeck('countess',8,False,False) #2
    prince1 = CardDeck('prince',5,False,False) #3
    prince2 = CardDeck('prince',5,False,False) #4
    handmaid = CardDeck('handmaid',4,False,False) #5
    priest1 = CardDeck('priest',2,False,False) #6
    priest2 = CardDeck('priest',2,False,False) #7
    baron1 = CardDeck('baron',3,False,False) #8 
    baron2 = CardDeck('baron',3,False,False) #9
    guard1 = CardDeck('guard',1,False,False) #10
    guard2 = CardDeck('guard',1,False,False) #11
    guard3 = CardDeck('guard',1,False,False) #12
    guard4 = CardDeck('guard',1,False,False) #13
    guard5 = CardDeck('guard',1,False,False) #14
    
    deck = [king,princess,countess,prince1,prince2,handmaid,priest1,priest2,baron1,baron2,guard1,guard2,guard3,guard4,guard5]
    
    return deck

def make_players():
    """simple method to create the players. intializes them to have names, 
    no round status or turn status, and no tokens in the beginning of the game"""
    player1 = Player('PLAYER 1', False, False, 0)
    player2 = Player('PLAYER 2', False, False, 0)
    return player1, player2
    

class GameKeeper:
    """keeps the players, cards, and stats for the game in a single class. an object of GameKeeper
    is created in main()
    from there it is editied as the game is played"""
    def __init__(self):
        self.round_number = 1
        self.gamers = make_players()
        
        """next two attributes keep track of 
        whose turn it is, and which player
        won the last round"""
        self.whose_turn_is_it_anyway = 0
        self.lastroundwinner = 0
        

        
        
    def shuffle(self):
        """creates a new player deck from scratch, intializing the deck
        to be entirely undealt"""
        self.player_cards = make_deck() 
        
    def deal(self,person):
        """deals cards to players by randomly selecting a card in the deck.
        if the card has been drawn, draw again"""
        print('\t')
        print('deal')
    
        
        sel = random.randint(0,14)
        #sel = 3        
        card_found = False
        while card_found != True:
            if self.player_cards[sel].dealt_status == False:
                self.gamers[person].hand.append(self.player_cards[sel])
                #note this is appending the list that contains a players hand
                self.player_cards[sel].dealt_status = True
                #sel = random.randint(0,14)
                ###################### debug print ###################
                print(self.gamers[person].player_name + ': ' + self.gamers[person].hand[0].card_name) 
                #prints just the first card in the players hand
                
                
                card_found = True
                #print(self.gamers[0].hand.card_name)
            
            
            else:
                sel = random.randint(0, 14)
    

        y = 1
        for z in range(15):
            if self.player_cards[z].dealt_status == True:
                y = y + 1
                self.num_cards_dealt = y
                print('dealt card:' + self.player_cards[z].card_name) 
                

class MainWin(QMainWindow):
    """create the main GUI window."""
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
        
    def initUI(self):
        """here we go"""
        
        #self.new_game = GameKeeper()
        self.last_guard_guess = 0 
        self.protected_status = 0
        self.first_move = 0
        #readyplayer1 = self.new_game.gamers[0].player_name
        #readyplayer2 = self.new_game.gamers[1].player_name
        #select_P1 = QPushButton('player2')
        
        self.menu = QMenuBar()
        self.rule_open = self.menu.addMenu("&Rules")
        
        
        self.menu_action=QAction('Love Letter Rules')
        self.menu_action.triggered.connect(self.rule_action)
        self.rule_open.addAction(self.menu_action)
        
        
        
        
        
        
        
        madisonsquaregarden = QMessageBox()
        welcome_text = 'Lets play a game. just kidding. welcome to love letter. let the tallest among you be player 1. are you READY PLAYER 1? see what i did there? okay enough lazy movie references, choose which among you most recently wrote a love letter and begin the game'
        madisonsquaregarden.setText(welcome_text)
        madisonsquaregarden.setIcon(QMessageBox.Question)
        madisonsquaregarden.addButton('player 1', QMessageBox.YesRole)
        madisonsquaregarden.addButton('player 2', QMessageBox.YesRole)
        #madisonsquaregarden.addButton()
        letter = madisonsquaregarden.exec()
        
        if letter:
            print('player 2')
            self.first_move = 2
        else:
            print('player 1')
            self.first_move = 1
        
        
        
        """rules action"""
        
        
        
        
        """player 1 subGUI on MainWin"""
        #namebox
        self.P1namebox = QLineEdit()
        self.P1namebox.setText('PLAYER 1')
        self.P1namebox.setReadOnly(True)
        self.P1namebox.setStyleSheet('font: 20px')
        self.P1namebox.setAlignment(Qt.AlignHCenter)
        self.P1namebox.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        
        #turn indicator
        self.P1turn = QRadioButton('turn', clicked=self.change_pic)
        self.P1turn.setCheckable(True)
        
        #make these a row layout
        self.P1row1 = QHBoxLayout()
        self.P1row1.addWidget(self.P1namebox)
        #self.P1row1.addWidget(self.P1turn)
        

        
        #card played this turn by player 1
        self.P1playedcard = QLabel()
        self.P1pic = QPixmap('blank.png')
        self.P1playedcard.setPixmap(self.P1pic)
        self.P1playedcard.setScaledContents(True)
        self.P1playedcard.setAlignment(Qt.AlignHCenter)
        self.P1playedcard.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)  
        
        #updating token count of player 1
        self.P1tokens = QLineEdit()
        self.P1tokens.setText('tokens: 0')
        self.P1tokens.setReadOnly(True)
        self.P1tokens.setAlignment(Qt.AlignHCenter)
        self.P1tokens.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        
        self.P1taketurn = QPushButton('take turn', clicked = self.player1taketurn)
        self.P1taketurn.setEnabled(False)
        self.P1taketurn.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        
        
        #make this all a layout for the LHS of the TOP of MainWin
        LHS = QVBoxLayout()
        LHS.addLayout(self.P1row1)
        #LHS.addWidget(P1namebox)
        #LHS.addWidget(self.P1roundstate)
        LHS.addWidget(self.P1playedcard)
        LHS.addWidget(self.P1tokens)
        LHS.addWidget(self.P1taketurn)
        

        """player 2 subGUI on MainWin"""
        #player 2 namebox
        self.P2namebox = QLineEdit()
        self.P2namebox.setText('PLAYER 2')
        self.P2namebox.setReadOnly(True)
        self.P2namebox.setStyleSheet('font: 20px')
        self.P2namebox.setAlignment(Qt.AlignHCenter)
        self.P2namebox.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        
        #turn indicator
        self.P2turn = QRadioButton('turn', clicked=self.change_pic)
        self.P2turn.setCheckable(True) 
        
        #make these a row layout
        self.P2row1 = QHBoxLayout()
        self.P2row1.addWidget(self.P2namebox)
        #self.P2row1.addWidget(self.P2turn)
        

        
        #card played this turn by player 1
        self.P2playedcard = QLabel()
        self.P2pic = QPixmap('blank.png')
        self.P2playedcard.setPixmap(self.P2pic)
        self.P2playedcard.setScaledContents(True)
        self.P2playedcard.setAlignment(Qt.AlignHCenter)
        self.P2playedcard.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)  
        
    #updating token count of player 1
        self.P2tokens = QLineEdit()
        self.P2tokens.setText('tokens: 0')
        self.P2tokens.setReadOnly(True)
        self.P2tokens.setAlignment(Qt.AlignHCenter)
        self.P2tokens.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        
        self.P2taketurn = QPushButton('take turn', clicked = self.player2taketurn)
        self.P2taketurn.setEnabled(False)
        self.P2taketurn.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        
        #make this all a layout for the RHS of the TOP of MainWin
        RHS = QVBoxLayout()
        RHS.addLayout(self.P2row1)
        #LHS.addWidget(P1namebox)
        #RHS.addWidget(self.P2roundstate)
        RHS.addWidget(self.P2playedcard)
        RHS.addWidget(self.P2tokens)
        RHS.addWidget(self.P2taketurn)
        
        #create the TOP row layout of MainWin
        TOP = QHBoxLayout()
        TOP.addLayout(LHS)
        TOP.addLayout(RHS)
        
        #FIXME: re-enable the discard slots on the GUI. then add discards in the StartNewRound() method


        """Bottom Row 1 subGUI for MainWin. contains the discarded cards.max discards set to 4 for now??"""
        self.discardlabel = QLineEdit()
        self.discardlabel.setText('\nCard Set Aside')
        self.discardlabel.setReadOnly(True)
        self.discardlabel.setAlignment(Qt.AlignHCenter)
        self.discardlabel.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        
        
        self.discard1 = QLabel()
        self.discard1pix = QPixmap('aside.png')
        self.discard1.setPixmap(self.discard1pix)
        self.discard1.setScaledContents(True)
        self.discard1.setAlignment(Qt.AlignHCenter)
        self.discard1.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        
        self.discard2 = QLabel()
        self.discard2pix = QPixmap('discarded.png')
        self.discard2.setPixmap(self.discard2pix)
        self.discard2.setScaledContents(True)
        self.discard2.setAlignment(Qt.AlignHCenter)
        self.discard2.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        
        self.discard3 = QLabel()
        self.discard3pix = QPixmap('discarded.png')
        self.discard3.setPixmap(self.discard3pix)
        self.discard3.setScaledContents(True)
        self.discard3.setAlignment(Qt.AlignHCenter)
        self.discard3.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        
        self.discard4 = QLabel()
        self.discard4pix = QPixmap('discarded.png')
        self.discard4.setPixmap(self.discard4pix)
        self.discard4.setScaledContents(True)
        self.discard4.setAlignment(Qt.AlignHCenter)
        self.discard4.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        
        B1 = QGridLayout()
        B1.addWidget(self.discardlabel,1,1)
        B1.addWidget(self.discard1,1,2)
        B1.addWidget(self.discard2,1,3)
        B1.addWidget(self.discard3,1,4)
        B1.addWidget(self.discard4,1,5)
        

        
        """bottom row 2 of the BOTTOM layout"""
        
        self.start_game = QPushButton('Start Game',clicked = self.StartGameMethod)
        self.start_game.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.next_round = QPushButton('Next Round', clicked = self.StartNewRound)
        self.next_round.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        
        self.round_indicator = QLineEdit()
        self.round_indicator.setText('Current Round: ')
        self.round_indicator.setReadOnly(True)
        self.round_indicator.setAlignment(Qt.AlignHCenter)
        self.round_indicator.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        
        self.result_indicator = QLineEdit()
        self.result_indicator.setText('Round Result: ')
        self.result_indicator.setReadOnly(True)
        self.result_indicator.setAlignment(Qt.AlignHCenter)
        self.result_indicator.setSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        
        
        
        B2R = QVBoxLayout()
        B2L = QVBoxLayout()

        B2R.addWidget(self.start_game)
        B2R.addWidget(self.next_round)
        B2L.addWidget(self.round_indicator)
        B2L.addWidget(self.result_indicator)

        BOTTOM = QHBoxLayout()
        BOTTOM.addLayout(B2L)  
        BOTTOM.addLayout(B2R)
        
        """create spacers for the MainWin to make the GUI cleaner"""
        self.spacer1 = QLabel()
        self.spacer1gap = QPixmap(700,20)
        self.spacer1gap.fill(Qt.black)
        self.spacer1.setPixmap(self.spacer1gap)
        self.spacer1.setScaledContents(True)
        self.spacer1.setAlignment(Qt.AlignHCenter)
        self.spacer1.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        
        self.spacer2 = QLabel()
        self.spacer2gap = QPixmap(700,20)
        self.spacer2gap.fill(Qt.black)
        self.spacer2.setPixmap(self.spacer2gap)
        self.spacer2.setScaledContents(True)
        self.spacer2.setAlignment(Qt.AlignHCenter)
        self.spacer2.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        
        #add the layouts and widgets to the full central widget layout
        fullwindow = QVBoxLayout()
        fullwindow.addWidget(self.menu)
        fullwindow.addLayout(TOP)
        fullwindow.addWidget(self.spacer1)
        fullwindow.addLayout(B1)
        fullwindow.addWidget(self.spacer2)
        fullwindow.addLayout(BOTTOM)
        
        
        central = QWidget()
        central.setLayout(fullwindow)
        
        
        #set the MainWin
        self.setCentralWidget(central)
        
    def rule_action(self):
        rules = QMessageBox()
        rules.setText('Here are the rules.')
        #QPixmap(pictoshow)
        rules.setIconPixmap(QPixmap('rules.png'))
        rules.exec()
        
        
        
        
    def change_pic(self):
        """placeholder method to update the picture of the card played"""
        
        ######################### debug print #############################
        #print('it changes')
        
        
        self.P1pic = QPixmap('baron.png')
        self.P1playedcard.setPixmap(self.P1pic)
        #self.P1roundstate.setText('out of round')
        self.new_game.gamers[0].tokens = 1 + self.new_game.gamers[0].tokens
        token = str('tokens: ') + str(self.new_game.gamers[0].tokens)
        self.P1tokens.setText(token)
        #self.P1roundstate.se
        #self.P1roundstate.
        self.show()
        
        
    def StartGameMethod(self):
        """initialize the game. must be done first"""
        
        print('\t')
        print('StartGameMethod')
        self.new_game = GameKeeper()
        self.new_game.shuffle()
        #print(self.new_game.gamers[0].player_name)
        
        
        #######    NEW STUFF
        self.new_game.discarded_cards = []
        a = 0
        while a < 4:
            pick_me = random.randint(0,14)
            if self.new_game.player_cards[pick_me].dealt_status == False:
                self.new_game.player_cards[pick_me].dealt_status = True
                self.new_game.discarded_cards.append(self.new_game.player_cards[pick_me])
                a = a + 1
            else:
                pick_me = random.randint(0,14)
        
        
        
        # CardToDiscard = random.randint(0, 14)
        # self.new_game.player_cards[CardToDiscard].dealt_status = True
        # self.new_game.num_cards_dealt = 1
        # #######create a new attribute to new_game. the cards that are discarded
        # self.new_game.discarded_cards = []
        # self.new_game.discarded_cards.append(self.new_game.player_cards[CardToDiscard])
        #print(self.new_game.player_cards[CardToDiscard].card_name + ' set aside?: ' + str(self.new_game.player_cards[CardToDiscard].dealt_status))
        print(self.new_game.discarded_cards[0].card_name + ' set aside?: ' + str(self.new_game.discarded_cards[0].dealt_status))
        print(self.new_game.discarded_cards[1].card_name + ' set face up?: ' + str(self.new_game.discarded_cards[1].dealt_status))
        print(self.new_game.discarded_cards[2].card_name + ' set face up?: ' + str(self.new_game.discarded_cards[2].dealt_status))
        print(self.new_game.discarded_cards[3].card_name + ' set face up?: ' + str(self.new_game.discarded_cards[3].dealt_status))
        
        self.new_game.deal(0)
        #self.new_game.deal(0)
        self.new_game.deal(1)
        print('\t')
        
        for i in range(15):
            print(self.new_game.player_cards[i].dealt_status)
        ############### debug print #######################
        if self.start_game.clicked:
            #print('its checked')
            self.start_game.setEnabled(False)
            #self.show()
        #print(self.new_game.player_cards[CardToDiscard].card_name + '.png')
        #self.discard1pix = QPixmap(self.new_game.player_cards[CardToDiscard].card_name + '.png')
        
        
        
        

        #####      NEW STUFF. deal the 3 cards face up for the two player game. 
        #deal 3 cards face up along side the set aside card (which is face down)
        self.discard1pix = QPixmap(self.new_game.discarded_cards[0].card_name + '.png')
        self.discard2pix = QPixmap(self.new_game.discarded_cards[1].card_name + '.png')
        self.discard3pix = QPixmap(self.new_game.discarded_cards[2].card_name + '.png')
        self.discard4pix = QPixmap(self.new_game.discarded_cards[3].card_name + '.png')

        # never set this to true. set the others to to
        #self.discard1.setPixmap(self.discard1pix)
        # set to true when ready
        self.discard2.setPixmap(self.discard2pix)
        self.discard3.setPixmap(self.discard3pix)
        self.discard4.setPixmap(self.discard4pix)
        
        
        
        
        
        
        self.round_indicator.setText('Current Round: 1')
        
        #changed to take in last love letter written argument for start of game
        
        if self.first_move == 1:
            self.new_game.whose_turn_is_it_anyway = 1
        else:
            self.new_game.whose_turn_is_it_anyway = 2
    
        if self.new_game.whose_turn_is_it_anyway == 1:
            self.P1taketurn.setEnabled(True)
            self.new_game.whose_turn_is_it_anyway = 2
        else:
            self.P2taketurn.setEnabled(True)
            self.new_game.whose_turn_is_it_anyway = 1
            
        
            
        
        
    
            
    def StartNewRound(self):
        """initiates a new round of love letter"""
        self.new_game.round_number = self.new_game.round_number + 1
        rounders = str('Current Round: ') + str(self.new_game.round_number)
        self.round_indicator.setText(rounders)
        self.result_indicator.setText('Round Result: ')
        
        self.new_game.shuffle()
        
        print('\t')
        print('StartNewRound')
        
        i = 0
        j = 0
        #CLEAR THE HANDS OF THE PLAYERS IN THE GAME
        for i in range(2):
            self.new_game.gamers[i].hand.clear()
            
        #: face up 3 card 
        #CLEAR THE DISCARDED CARDS PILE
        self.new_game.discarded_cards.clear()
        a = 0
        while a < 4:
            pick_me = random.randint(0,14)
            if self.new_game.player_cards[pick_me].dealt_status == False:
                self.new_game.player_cards[pick_me].dealt_status = True
                self.new_game.discarded_cards.append(self.new_game.player_cards[pick_me])
                a = a + 1
            else:
                pick_me = random.randint(0,14)
                
        print(self.new_game.discarded_cards[0].card_name + ' set aside?: ' + str(self.new_game.discarded_cards[0].dealt_status))
        print(self.new_game.discarded_cards[1].card_name + ' set face up?: ' + str(self.new_game.discarded_cards[1].dealt_status))
        print(self.new_game.discarded_cards[2].card_name + ' set face up?: ' + str(self.new_game.discarded_cards[2].dealt_status))
        print(self.new_game.discarded_cards[3].card_name + ' set face up?: ' + str(self.new_game.discarded_cards[3].dealt_status))
        
        
        
        #CardToDiscard1 = random.randint(0, 14)

        #self.new_game.player_cards[CardToDiscard1].dealt_status = True

        
        #DEAL NEW CARDS TO THE PLAYERS
        self.new_game.deal(0)
        self.new_game.deal(1)
        #CardToDiscard = random.randint(0, 14)
        #self.new_game.player_cards[CardToDiscard].dealt_status = True
        #print(self.new_game.player_cards[CardToDiscard1].card_name + ' set aside : ' + str(self.new_game.player_cards[CardToDiscard1].dealt_status))
        #
        
        #self.new_game.discarded_cards.append(self.new_game.player_cards[CardToDiscard1])
        
        
        
        #: deal 3 cards face up along side the set aside card (which is face down)
        #self.discard1pix = QPixmap(self.new_game.discarded_cards[0].card_name + '.png')
        self.discard2pix = QPixmap(self.new_game.discarded_cards[1].card_name + '.png')
        self.discard3pix = QPixmap(self.new_game.discarded_cards[2].card_name + '.png')
        self.discard4pix = QPixmap(self.new_game.discarded_cards[3].card_name + '.png')

        
        #: never set this to true. set the others to to
        #self.discard1.setPixmap(self.discard1pix)
        self.discard2.setPixmap(self.discard2pix)
        self.discard3.setPixmap(self.discard3pix)
        self.discard4.setPixmap(self.discard4pix)

        #print(self.new_game.gamers[0].hand[0])
        
        print('dealt statuses2:')
        for k in range(15):
            print(self.new_game.player_cards[k].dealt_status)
            
        # if self.new_game.lastroundwinner == 0:
        #     self.P1taketurn.setEnabled(True)
        # else:
        #     self.P2taketurn.setEnabled(True)
            

        self.P1taketurn.setEnabled(False)
        self.P2taketurn.setEnabled(False)
        
        # if self.new_game.lastroundwinner == 0:
        #     #for the very start of the game
        #     if self.new_game.whose_turn_is_it_anyway == 1:
        #         self.P1taketurn.setEnabled(True)
        #         self.new_game.whose_turn_is_it_anyway = 2
        #     else:
        #         self.P2taketurn.setEnabled(True)
        #         self.new_game.whose_turn_is_it_anyway = 1
                
        if self.new_game.lastroundwinner == 1:
            #player 1 won last round. they start new round
            self.P1taketurn.setEnabled(True)
            self.new_game.whose_turn_is_it_anyway = 1
        elif self.new_game.lastroundwinner == 2:
            self.P2taketurn.setEnabled(True)
            self.new_game.whose_turn_is_it_anyway = 2
        else:
            print('something is wrong here')
            
        #REMOVE PLAYED CARD PICTURES
        self.P1pic = QPixmap('blank.png')
        self.P1playedcard.setPixmap(self.P1pic)
        self.P2pic = QPixmap('blank.png')
        self.P2playedcard.setPixmap(self.P2pic)
        
        self.new_game.gamers[0].protected_status == False
        self.new_game.gamers[1].protected_status == False
        
        
        
            

            
            
        
            
            
    def player1taketurn(self):
        print('\t')
        print('player1taketurn')
        print('cards dealt: '+str(self.new_game.num_cards_dealt))


        if self.new_game.num_cards_dealt <=15:
        
            self.new_game.deal(0)
            self.P1_card_played = FormWindowP1()
            self.P1_card_played.cards_to_pass(self.new_game.gamers[0].hand)
            self.P1_card_played.showandtell()
            #self.P1_card_played.submitted1[int].connect(self.onSubmitted1)
            self.P1_card_played.submitted1[object].connect(self.onSubmitted1)
            if self.P1taketurn.clicked:
                self.P1taketurn.setEnabled(False)
                self.P2taketurn.setEnabled((True))
        else:
            print('draw the aside card')
            self.new_game.gamers[0].hand.append(self.new_game.discarded_cards[0])
            self.P1_card_played.cards_to_pass(self.new_game.gamers[0].hand)
            self.P1_card_played.showandtell()
            #self.P1_card_played.submitted1[int].connect(self.onSubmitted1)
            self.P1_card_played.submitted1[object].connect(self.onSubmitted1)
            if self.P1taketurn.clicked:
                self.P1taketurn.setEnabled(False)
                self.P2taketurn.setEnabled((True))

    
    def player2taketurn(self):
        print('\t')
        print('player2taketurn')
        print('cards dealt: '+str(self.new_game.num_cards_dealt))

        
        if self.new_game.num_cards_dealt <=15:

            self.new_game.deal(1)
            self.P2_card_played = FormWindowP2()
            self.P2_card_played.cards_to_pass(self.new_game.gamers[1].hand)
            self.P2_card_played.showandtell()
            #self.P1_card_played.submitted1[int].connect(self.onSubmitted1)
            self.P2_card_played.submitted2[object].connect(self.onSubmitted2)
            if self.P2taketurn.clicked:
                self.P2taketurn.setEnabled(False)
                self.P1taketurn.setEnabled(True)
        else:
            print('ran out of cards yo')
            self.new_game.gamers[1].hand.append(self.new_game.discarded_cards[0])
            self.P2_card_played = FormWindowP2()
            self.P2_card_played.cards_to_pass(self.new_game.gamers[1].hand)
            self.P2_card_played.showandtell()
            #self.P1_card_played.submitted1[int].connect(self.onSubmitted1)
            self.P2_card_played.submitted2[object].connect(self.onSubmitted2)
            if self.P2taketurn.clicked:
                self.P2taketurn.setEnabled(False)
                self.P1taketurn.setEnabled(True)
            
    
    def Card_Evaluation(self,card_in_question,sender,recursive = False):
        """the most important aspect of the game. evaluate the card played 
        (card_in_question) each turn by the player (sender). if comparisons are necessary,
        evaluate other player hand"""
        
        """RECURSION: the recursive flag is for the guard only.
        if a guard is played, the player that played it must guess a card. a form
        window allows this. this card is then passed back into the Card_Evaluation
        method as the card_in_quesion arguement, during the same turn, making it a psuedo-recursive call.
        the second call evaluates the guessed card within the guard guess framework"""
        
        if recursive == True:
            self.card_being_played.card_name = 'guard'
        
        else:
            self.card_being_played = card_in_question
        #text = self.card_being_played.effect
        
        #######     BARON     ######
        if self.card_being_played.card_name == 'baron':
            #compare hands. winner is player with higher effect card
            print(str(sender) + ' played ' + 'the baron')
            print('P1 card in hand: ' + self.new_game.gamers[0].hand[0].card_name)
            print('P2 card in hand: ' + self.new_game.gamers[1].hand[0].card_name)
            print('P1 protected status:' + str(self.new_game.gamers[0].protected_status))
            print('P2 protected status:' + str(self.new_game.gamers[1].protected_status))
            if sender == 1 and self.new_game.gamers[1].protected_status == False:
                    
                if self.new_game.gamers[0].hand[0].effect > self.new_game.gamers[1].hand[0].effect:
                    print('\t')
    
                    print('!!!!!!player 1 wins round!!!!!')
                    print('\t')
                    self.new_game.gamers[0].tokens = self.new_game.gamers[0].tokens + 1
                    token = str('tokens: ') + str(self.new_game.gamers[0].tokens)
                    self.P1tokens.setText(token)
                    self.new_game.lastroundwinner = 1
                    self.P1taketurn.setEnabled(False)
                    self.P2taketurn.setEnabled(False)
                    resolution = 'Round Result: ' + 'Player 1 wins round'
                    self.result_indicator.setText(resolution)
                    #self.StartNewRound()
                else:
                    print('\t')
                    print('!!!!!!player 2 wins round!!!!!')
                    self.new_game.gamers[1].tokens = self.new_game.gamers[1].tokens + 1
                    token = str('tokens: ') + str(self.new_game.gamers[1].tokens)
                    self.P2tokens.setText(token)
                    self.new_game.lastroundwinner=2
                    self.P1taketurn.setEnabled(False)
                    self.P2taketurn.setEnabled(False)
                    resolution = 'Round Result: ' + 'Player 2 wins round'
                    self.result_indicator.setText(resolution)
                    #self.StartNewRound()
                    print('\t')
            elif sender ==2 and self.new_game.gamers[0].protected_status == False:
                if self.new_game.gamers[1].hand[0].effect > self.new_game.gamers[0].hand[0].effect:
                    print('\t')
                    print('!!!!!!player 2 wins round!!!!!')
                    self.new_game.gamers[1].tokens = self.new_game.gamers[1].tokens + 1
                    token = str('tokens: ') + str(self.new_game.gamers[1].tokens)
                    self.P2tokens.setText(token)
                    self.new_game.lastroundwinner = 2
                    self.P1taketurn.setEnabled(False)
                    self.P2taketurn.setEnabled(False)
                    resolution = 'Round Result: ' + 'Player 2 wins round'
                    self.result_indicator.setText(resolution)
                    #self.StartNewRound()
                    print('\t')
                else:
                    print('\t')
                    print('!!!!!!player 1 wins round!!!!!')
                    self.new_game.gamers[0].tokens = self.new_game.gamers[0].tokens + 1
                    token = str('tokens: ') + str(self.new_game.gamers[0].tokens)
                    self.P1tokens.setText(token)
                    self.new_game.lastroundwinner = 1
                    self.P1taketurn.setEnabled(False)
                    self.P2taketurn.setEnabled(False)
                    resolution = 'Round Result: ' + 'Player 1 wins round'
                    self.result_indicator.setText(resolution)
                    #self.StartNewRound()
                    print('\t')
                    
            #protection of the haindmaid
            elif sender ==1 and self.new_game.gamers[1].protected_status == True:
                pass
            elif sender == 2 and self.new_game.gamers[0].protected_status == True:
                pass
            else:
                print('baron problem')
                pass
                    
        #####     PRIEST     #####
        elif self.card_being_played.card_name == 'priest':
            #show the hand of the other player
            print(str(sender) + ' played ' + 'the the priest')
            print('P1 card in hand: ' + self.new_game.gamers[0].hand[0].card_name)
            print('P2 card in hand: ' + self.new_game.gamers[1].hand[0].card_name)
            print('P1 protected status:' + str(self.new_game.gamers[0].protected_status))
            print('P2 protected status:' + str(self.new_game.gamers[1].protected_status))
            if sender == 1 and self.new_game.gamers[1].protected_status == False:
                #player 2 shows player 1 their card
                pictoshow = self.new_game.gamers[1].hand[0].card_name + '.png'
                showmewhatyougot = QMessageBox()
                showmewhatyougot.setText('player 2 hand: ')
                showmewhatyougot.setIconPixmap(QPixmap(pictoshow))
                showmewhatyougot.exec()
            elif sender == 2 and self.new_game.gamers[0].protected_status == False:
                #player 1 shows player 2 their cards
                pictoshow = self.new_game.gamers[0].hand[0].card_name + '.png'
                showmewhatyougot = QMessageBox()
                showmewhatyougot.setText('player 1 hand: ')
                showmewhatyougot.setIconPixmap(QPixmap(pictoshow))
                showmewhatyougot.exec()
            elif sender == 1 and self.new_game.gamers[1].protected_status == True:
                print('to be fair...')
                pass
            elif sender == 2 and self.new_game.gamers[0].protected_status == True:
                pass
            else:
                pass

        #####     THE KING IN THE NORTH     #####
        elif self.card_being_played.card_name == 'king':
            
            if sender == 1 and self.new_game.gamers[1].protected_status == False:
            
                print(str(sender) + ' played ' + 'the the king')
                print('P1 card in hand: ' + self.new_game.gamers[0].hand[0].card_name)
                print('P2 card in hand: ' + self.new_game.gamers[1].hand[0].card_name)
    
                #players swap hands
                holder = self.new_game.gamers[0].hand[0]
                self.new_game.gamers[0].hand[0] = self.new_game.gamers[1].hand[0]
                self.new_game.gamers[1].hand[0] = holder
                print('\t')
                print('after swap:')            
                print('P1 card in hand: ' + self.new_game.gamers[0].hand[0].card_name)
                print('P2 card in hand: ' + self.new_game.gamers[1].hand[0].card_name)
                
            elif sender == 2 and self.new_game.gamers[0].protected_status == False:
                print(str(sender) + ' played ' + 'the the king')
                print('P1 card in hand: ' + self.new_game.gamers[0].hand[0].card_name)
                print('P2 card in hand: ' + self.new_game.gamers[1].hand[0].card_name)
    
                #players swap hands
                holder = self.new_game.gamers[0].hand[0]
                self.new_game.gamers[0].hand[0] = self.new_game.gamers[1].hand[0]
                self.new_game.gamers[1].hand[0] = holder
                print('\t')
                print('after swap:')            
                print('P1 card in hand: ' + self.new_game.gamers[0].hand[0].card_name)
                print('P2 card in hand: ' + self.new_game.gamers[1].hand[0].card_name)
            else:
                pass
            
        ##### PRINCESS #####
        elif self.card_being_played.card_name == 'princess':
            if sender == 1:
                print(str(sender) + ' played ' + 'the princess')
                print('player 2 wins round')
                resolution = 'Round Result: ' + 'Player 2 wins round'
                self.result_indicator.setText(resolution)
                self.new_game.gamers[1].tokens = self.new_game.gamers[1].tokens + 1
                token = str('tokens: ') + str(self.new_game.gamers[1].tokens)
                self.P2tokens.setText(token)
                self.new_game.lastroundwinner = 2
                self.P1taketurn.setEnabled(False)
                self.P2taketurn.setEnabled(False)
            elif sender == 2:
                print(str(sender) + ' played ' + 'the princess')
                print('player 1 wins round')
                resolution = 'Round Result: ' + 'Player 1 wins round'
                self.result_indicator.setText(resolution)
                self.new_game.gamers[0].tokens = self.new_game.gamers[0].tokens + 1
                token = str('tokens: ') + str(self.new_game.gamers[0].tokens)
                self.P1tokens.setText(token)
                self.new_game.lastroundwinner = 1
                self.P1taketurn.setEnabled(False)
                self.P2taketurn.setEnabled(False)
            else:
                print('degens from up country')
                
        #####     THE PRINCE THAT WAS PROMISED     ######
        elif self.card_being_played.card_name == 'prince':
            choose_player = QMessageBox()
            display_text = 'choose a player to discard their hand, including yourself'
            choose_player.setText(display_text)
            choose_player.addButton('player1',QMessageBox.YesRole)
            choose_player.addButton('player2',QMessageBox.YesRole)
            chosen = choose_player.exec()
            
            
            # handmaid protection is top if statement
            # chosen == 1 is p2, chosen == 0 is p1
            
            if (sender == 1 and self.new_game.gamers[chosen].protected_status == False) or (sender == 2 and self.new_game.gamers[chosen].protected_status == False):
            
            
                if chosen:
                    print('player 2 was chosen')
                    if self.new_game.gamers[1].hand[0].card_name == 'princess':
                        result = 'Round Result: '+'round is over. P1 wins. P2 discarded princess'
                        self.result_indicator.setText(result)
                        self.new_game.gamers[0].tokens = self.new_game.gamers[0].tokens + 1
                        token = str('tokens: ') + str(self.new_game.gamers[0].tokens)
                        self.P1tokens.setText(token)
                        self.new_game.lastroundwinner = 1
                        self.P1taketurn.setEnabled(False)
                        self.P2taketurn.setEnabled(False)                    
                    else:
                        self.new_game.gamers[1].hand.pop(0)
                        if self.new_game.num_cards_dealt < 15:
                            self.new_game.deal(1)
                        else:
                            #if the deck runs out, pull the set aside (discarded) card 
                            self.new_game.gamers[1].hand.append(self.new_game.discarded_cards[0])
                        
                else:
                    print('player1 was chosen')
                    if self.new_game.gamers[0].hand[0].card_name == 'princess':
                        result = 'Round Result: '+'round is over. P2 wins. P1 discarded princess'
                        self.result_indicator.setText(result)
                        self.new_game.gamers[1].tokens = self.new_game.gamers[1].tokens + 1
                        token = str('tokens: ') + str(self.new_game.gamers[1].tokens)
                        self.P2tokens.setText(token)
                        self.new_game.lastroundwinner = 2
                        self.P1taketurn.setEnabled(False)
                        self.P2taketurn.setEnabled(False) 
                        
                    else:
                        self.new_game.gamers[0].hand.pop(0)
                        if self.new_game.num_cards_dealt < 15:
                            self.new_game.deal(0)
                        else:
                            #if the deck runs out, pull the set aside (discarded) card 
                            self.new_game.gamers[0].hand.append(self.new_game.discarded_cards[0])
                            
            else:
                pass
                        


        ##### COUNTESS ######
        elif self.card_being_played.card_name ==  'countess':
            pass
        
        ##### THE HANDMAIDS TALE #####
    
        elif self.card_being_played.card_name == 'handmaid':
            if sender == 1:
                self.new_game.gamers[0].protected_status = True
                print('P1 protect: '+str(self.new_game.gamers[0].protected_status))
                
                print('P2 protect: '+str(self.new_game.gamers[1].protected_status))
                
            elif sender == 2:
                self.new_game.gamers[1].protected_status = True
                print('P1 protect: '+str(self.new_game.gamers[0].protected_status))
                print('P2 protect: '+str(self.new_game.gamers[1].protected_status))
            else:
                pass
        
        ##### GUARD #####
        elif self.card_being_played.card_name == 'guard':
            
            
            if recursive == False:
                self.guess = FormWindow3()
                self.guess.submitted3[str].connect(self.onSubmitted3)
                self.last_guard_guess = sender
            else:
                if self.last_guard_guess == 1 and self.new_game.gamers[1].protected_status == False:
                    if card_in_question == self.new_game.gamers[1].hand[0].card_name:
                        result = 'Round Result: '+'round is over. P1 wins. P1 guesses P2 hand correctly'
                        self.result_indicator.setText(result)
                        self.new_game.gamers[0].tokens = self.new_game.gamers[0].tokens + 1
                        token = str('tokens: ') + str(self.new_game.gamers[0].tokens)
                        self.P1tokens.setText(token)
                        self.new_game.lastroundwinner = 1
                        self.P1taketurn.setEnabled(False)
                        self.P2taketurn.setEnabled(False)
                        
                    else:
                        pass
                    
                elif self.last_guard_guess == 2 and self.new_game.gamers[0].protected_status == False:
                    if card_in_question == self.new_game.gamers[0].hand[0].card_name:
                        result = 'Round Result: '+'round is over. P2 wins. P2 giesses P1 hand correctly'
                        self.result_indicator.setText(result)
                        self.new_game.gamers[1].tokens = self.new_game.gamers[1].tokens + 1
                        token = str('tokens: ') + str(self.new_game.gamers[1].tokens)
                        self.P2tokens.setText(token)
                        self.new_game.lastroundwinner = 2
                        self.P1taketurn.setEnabled(False)
                        self.P2taketurn.setEnabled(False) 
                    else:
                        pass
                elif self.last_guard_guess == 1 and self.new_game.gamers[1].protected_status == True:
                    pass
                elif self.last_guard_guess == 2 and self.new_game.gamers[0].protected_status == True:
                    pass
                else:
                    pass
                        
                #     #works if 2 consecuive guard are played and king selected. does not work concurrently
                #     print('THATS WHAT I APPRECIATES ABOUT YOU SQUIRELY DAN')
                # elif card_in_question == 'princess':
                #     print('IF I WERE A DR. SEUSS BOOK ID BE THE FAT IN THE HAT')
            

        else:
            pass
        
    
        """game winner condition evaluated and set here"""
        if self.new_game.gamers[0].tokens == 6:
            self.P1taketurn.setEnabled(False)
            self.P2taketurn.setEnabled(False)
            self.next_round.setEnabled(False)
            self.round_indicator.setText('PLAYER 1 WINS')
            WINNER = QMessageBox()
            WINNER.setText('PLAYER 1 WINS')
            WINNER.exec()
            
        elif self.new_game.gamers[1].tokens == 6:
            self.P1taketurn.setEnabled(False)
            self.P2taketurn.setEnabled(False)
            self.next_round.setEnabled(False)
            self.round_indicator.setText('PLAYER 2 WINS')
            WINNER = QMessageBox()
            WINNER.setText('PLAYER 2 WINS')
            WINNER.exec()
            
        else:
            pass
            
            
    def onSubmitted1(self, integer):
        """recieves the card to be played as an abstract object.
        also removes said card from the players hand. then sends that card to the 
        Card_Evaluator. integer is left over from when the signal passed back an int"""
        self.someval = integer
        print('\n')
        print('onbubmitted1')
        print('recieved: ' + str(self.someval.effect))
        print('p1card1: '+self.new_game.gamers[0].hand[0].card_name)
        print('p1card2: '+self.new_game.gamers[0].hand[1].card_name)
        #print(type(self.someval.index_to_delte)) # this works in printing the index to be removed
        self.new_game.gamers[0].hand.pop(self.someval.index_to_delte)
        print('p1card1now: '+self.new_game.gamers[0].hand[0].card_name)
        self.P1pic = QPixmap(self.someval.card_name + '.png')
        self.P1playedcard.setPixmap(self.P1pic)
        print('dealt status after card play:')
        for k in range(15):
            print(self.new_game.player_cards[k].dealt_status)
        #self.new_game.Card_Evaluator(self.someval,1)
        self.Card_Evaluation(self.someval, 1)
        
    def onSubmitted2(self,integer):
        self.someval = integer
        print('\n')
        print('onbubmitted2')
        print('recieved: ' + str(self.someval.effect))
        print('p2card1: '+self.new_game.gamers[1].hand[0].card_name)
        print('p2card2: '+self.new_game.gamers[1].hand[1].card_name)
        #print(type(self.someval.index_to_delte)) # this works in printing the index to be removed
        self.new_game.gamers[1].hand.pop(self.someval.index_to_delte)
        print('p2card1now: '+self.new_game.gamers[1].hand[0].card_name)
        self.P2pic = QPixmap(self.someval.card_name + '.png')
        self.P2playedcard.setPixmap(self.P2pic)
        print('dealt status after card play:')
        for k in range(15):
            print(self.new_game.player_cards[k].dealt_status)
        #self.new_game.Card_Evaluator(self.someval,2)
        #self.teval()
        self.Card_Evaluation(self.someval, 2)
        
    def onSubmitted3(self,string):
        self.guard_guesses = string
        self.Card_Evaluation(self.guard_guesses, 1,True)
        

            

            
        
        
        

class FormWindowP1(QtWidgets.QTabWidget):
    """form window for the turn based part of the game. each player shouldn't
    see the others cards, so a window will appear on each players turn 
    upon pressing their hand button"""
    #submitted1 = QtCore.pyqtSignal([int])
    submitted1 = QtCore.pyqtSignal([object])
    
    
    def __init__(self):
        super().__init__()
        

        
    def cards_to_pass(self,cards):
        """takes the card played by the player. evaluates for the countess condition
        stores the hand in an attribute, which moves on to be submitted"""
        self.P1hand = cards
        print('\t')
        print('cards passed by player1:')
        print(self.P1hand[0].card_name)
        print(self.P1hand[1].card_name)
        ######## implement the countess #####
        self.must_play_countess = False
        self.must_play_countess_index = 0
        if self.P1hand[0].card_name == 'countess':
            if self.P1hand[1].card_name == 'king' or self.P1hand[1].card_name == 'prince':
                self.must_play_countess = True
                self.must_play_countess_index = 0

        elif self.P1hand[1].card_name == 'countess':

            if self.P1hand[0].card_name == 'king' or self.P1hand[0].card_name == 'prince':
                self.must_play_countess = True
                self.must_play_countess_index = 1
        else:
            pass
        if self.must_play_countess == True:
            WINNER1 = QMessageBox()
            WINNER1.setText('you must play the countess. sorry. rules are rules. but you can try to play the other card if you want')
            WINNER1.exec()
            self.onSubmit1()
            #print('COUNTESS!!!!!!!!!')

        #print(self.P1hand[0].effect)
        
    def showandtell(self):
        self.heading = QLabel('PLAYER 1 TURN')
        self.heading.setSizePolicy(QtWidgets.QSizePolicy.Fixed,QtWidgets.QSizePolicy.Fixed)
        
        gridlayout = QGridLayout()
        rowheading = QHBoxLayout()
        rowheading.addWidget(self.heading)
        gridlayout.addWidget(self.heading,1,2)
        
        
        self.P1_in_hand = QLabel()
        self.P1_in_hand_pic = QPixmap(self.P1hand[0].card_name + '.png')
        self.P1_in_hand.setPixmap(self.P1_in_hand_pic)
        self.P1_in_hand.setScaledContents(True)
        self.P1_in_hand.setAlignment(Qt.AlignHCenter)
        self.P1_in_hand.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        
        self.P1_drawn = QLabel()
        self.P1_drawn_pic = QPixmap(self.P1hand[1].card_name + '.png')
        self.P1_drawn.setPixmap(self.P1_drawn_pic)
        self.P1_drawn.setScaledContents(True)
        self.P1_drawn.setAlignment(Qt.AlignHCenter)
        self.P1_drawn.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        
        self.P1_hand_label = QLineEdit()
        self.P1_hand_label.setText('In Hand')
        self.P1_hand_label.setReadOnly(True)
        self.P1_hand_label.setAlignment(Qt.AlignHCenter)
        self.P1_hand_label.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)

        self.P1_drawn_label = QLineEdit()
        self.P1_drawn_label.setText('Deck Draw')
        self.P1_drawn_label.setReadOnly(True)
        self.P1_drawn_label.setAlignment(Qt.AlignHCenter)
        self.P1_drawn_label.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        
        
        self.P1_selection1 = QRadioButton('choose card')
        self.P1_selection1.setCheckable(True)
        
        self.P1_selection2 = QRadioButton('choose card')
        self.P1_selection2.setCheckable(True)
        
        self.P1_play_button = QPushButton('play chosen card',clicked = self.onSubmit1)
        self.P1_play_button.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        
        
           
        #set the final layout here
        gridlayout.addWidget(self.P1_in_hand,2,1)
        gridlayout.addWidget(self.P1_drawn,2,2)
        gridlayout.addWidget(self.P1_hand_label,3,1)
        gridlayout.addWidget(self.P1_drawn_label,3,2)
        gridlayout.addWidget(self.P1_selection1,4,1)
        gridlayout.addWidget(self.P1_selection2,4,2)
        gridlayout.addWidget(self.P1_play_button,4,3)
        self.setLayout(gridlayout)
        self.show()
        
        
    def onSubmit1(self):
        print('\t')
        print('onSubmit1')


        if self.must_play_countess == True:

            if self.must_play_countess_index == 0:
                self.P1hand[0].index_to_delte = 0
                toSend1 = self.P1hand[0]
                self.submitted1[object].emit(toSend1)
                self.close()
            elif self.must_play_countess_index == 1:
                self.P1hand[1].index_to_delte = 1
                toSend1 = self.P1hand[1]
                self.submitted1[object].emit(toSend1)
                self.close()
            else:
                pass
        
        else:    

            if self.P1_selection1.isChecked():
                #print('\n')
                print('sent: '+ str(self.P1hand[0].effect))
                #set the index of the player hand to be deleted, as the card played must be removed from hand
                self.P1hand[0].index_to_delte = 0
                toSend1 = self.P1hand[0]
                self.submitted1[object].emit(toSend1)
                self.close()
            elif self.P1_selection2.isChecked():
                #print('\n')
                print('sent: '+ str(self.P1hand[1].effect))
                #set the index of the player hand to be deleted, as the card played must be removed from hand
                self.P1hand[1].index_to_delte = 1
                toSend1 = self.P1hand[1]
                self.submitted1[object].emit(toSend1)
                self.close()           
        
        

class FormWindowP2(QtWidgets.QTabWidget):
    """form window for the turn based part of the game. each player shouldn't
    see the others cards, so a window will appear on each players turn 
    upon pressing their hand button"""
    #submitted1 = QtCore.pyqtSignal([int])
    submitted2 = QtCore.pyqtSignal([object])
    
    
    def __init__(self):
        super().__init__()
        

        
    def cards_to_pass(self,cards):
        self.P2hand = cards
        print('\t')
        print('cards passed by player2:')
        print(self.P2hand[0].card_name)
        print(self.P2hand[1].card_name)
        #print(self.P1hand[0].effect)
        self.must_play_countess = False
        self.must_play_countess_index = 0
        
        
        #takes care of the countess evaluation problem. not elegant. 
        if self.P2hand[0].card_name == 'countess':
            if self.P2hand[1].card_name == 'king' or self.P2hand[1].card_name == 'prince':
                self.must_play_countess = True
                self.must_play_countess_index = 0
                
        elif self.P2hand[1].card_name == 'countess':
            if self.P2hand[0].card_name == 'king' or self.P2hand[0].card_name == 'prince':
                self.must_play_countess = True
                self.must_play_countess_index = 1
                
        else:
            #print('MISTAKE')
            pass
        
        if self.must_play_countess == True:
            WINNER2 = QMessageBox()
            WINNER2.setText('you must play the countess. sorry. rules are rules. but you can try to play the other card if you want')
            WINNER2.exec()
            self.onSubmit2()
        
    def showandtell(self):
        self.heading = QLabel('PLAYER 2 TURN')
        self.heading.setSizePolicy(QtWidgets.QSizePolicy.Fixed,QtWidgets.QSizePolicy.Fixed)
        
        gridlayout = QGridLayout()
        rowheading = QHBoxLayout()
        rowheading.addWidget(self.heading)
        gridlayout.addWidget(self.heading,1,2)
        
        
        self.P2_in_hand = QLabel()
        self.P2_in_hand_pic = QPixmap(self.P2hand[0].card_name + '.png')
        self.P2_in_hand.setPixmap(self.P2_in_hand_pic)
        self.P2_in_hand.setScaledContents(True)
        self.P2_in_hand.setAlignment(Qt.AlignHCenter)
        self.P2_in_hand.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        
        self.P2_drawn = QLabel()
        self.P2_drawn_pic = QPixmap(self.P2hand[1].card_name + '.png')
        self.P2_drawn.setPixmap(self.P2_drawn_pic)
        self.P2_drawn.setScaledContents(True)
        self.P2_drawn.setAlignment(Qt.AlignHCenter)
        self.P2_drawn.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        
        self.P2_hand_label = QLineEdit()
        self.P2_hand_label.setText('In Hand')
        self.P2_hand_label.setReadOnly(True)
        self.P2_hand_label.setAlignment(Qt.AlignHCenter)
        self.P2_hand_label.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)

        self.P2_drawn_label = QLineEdit()
        self.P2_drawn_label.setText('Deck Draw')
        self.P2_drawn_label.setReadOnly(True)
        self.P2_drawn_label.setAlignment(Qt.AlignHCenter)
        self.P2_drawn_label.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        
        
        self.P2_selection1 = QRadioButton('choose card')
        self.P2_selection1.setCheckable(True)
        
        self.P2_selection2 = QRadioButton('choose card')
        self.P2_selection2.setCheckable(True)
        
        self.P2_play_button = QPushButton('play chosen card',clicked = self.onSubmit2)
        self.P2_play_button.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        
        
           
        #set the final layout here
        gridlayout.addWidget(self.P2_in_hand,2,1)
        gridlayout.addWidget(self.P2_drawn,2,2)
        gridlayout.addWidget(self.P2_hand_label,3,1)
        gridlayout.addWidget(self.P2_drawn_label,3,2)
        gridlayout.addWidget(self.P2_selection1,4,1)
        gridlayout.addWidget(self.P2_selection2,4,2)
        gridlayout.addWidget(self.P2_play_button,4,3)
        self.setLayout(gridlayout)
        self.show()
        
        
    def onSubmit2(self):
        print('\t')
        print('onSubmit2')

        if self.must_play_countess == True:
            if self.must_play_countess_index == 0:
                self.P2hand[0].index_to_delte = 0
                toSend2 = self.P2hand[0]
                self.submitted2[object].emit(toSend2)
                self.close()
            elif self.must_play_countess_index == 1:
                self.P2hand[1].index_to_delte = 1
                toSend2 = self.P2hand[1]
                self.submitted2[object].emit(toSend2)
                self.close()
            else:
                pass
                print('MISTAKE')
        
        else:

            if self.P2_selection1.isChecked():
                #print('\n')
                print('sent: '+ str(self.P2hand[0].effect))
                #set the index of the player hand to be deleted, as the card played must be removed from hand
                self.P2hand[0].index_to_delte = 0
                toSend2 = self.P2hand[0]
                self.submitted2[object].emit(toSend2)
                self.close()
            elif self.P2_selection2.isChecked():
                #print('\n')
                print('sent: '+ str(self.P2hand[1].effect))
                #set the index of the player hand to be deleted, as the card played must be removed from hand
                self.P2hand[1].index_to_delte = 1
                toSend2 = self.P2hand[1]
                self.submitted2[object].emit(toSend2)
                self.close()        
                
                
class FormWindow3(QtWidgets.QTabWidget):
    """a long window that allows selection of card to be guessed in other players hand"""
    submitted3 = QtCore.pyqtSignal([str])
    
    def __init__(self):
        super().__init__()            
        
        self.label = QLabel('guess card of other player: ')
        self.label.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        
        self.king_button = QPushButton('king', clicked = self.king)
        self.king_button.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        
        self.princess_button = QPushButton('princess', clicked = self.princess)
        self.princess_button.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        
        self.countess_button = QPushButton('countess', clicked = self.countess)
        self.countess_button.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        
        self.prince_button = QPushButton('prince', clicked = self.prince)
        self.prince_button.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        
        self.handmaid_button = QPushButton('handmaid', clicked = self.handmaid)
        self.handmaid_button.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        
        self.priest_button = QPushButton('priest', clicked = self.priest)
        self.priest_button.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        
        self.baron_button = QPushButton('baron', clicked = self.baron)
        self.baron_button.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        
        self.guard_button = QPushButton('guard', clicked = self.guard)
        self.guard_button.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
    
        
        self.layout = QHBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.king_button)
        self.layout.addWidget(self.princess_button)
        self.layout.addWidget(self.countess_button)
        self.layout.addWidget(self.prince_button)
        self.layout.addWidget(self.handmaid_button)
        self.layout.addWidget(self.priest_button)
        self.layout.addWidget(self.baron_button)
        #self.layout.addWidget(self.guard_button)
        self.setLayout(self.layout)
        self.show()
        


    def king(self):
        self.submitted3[str].emit('king')
        self.give_back = 'king'
        self.close()
    def princess(self):
        self.submitted3[str].emit('princess')
        self.give_back = 'princess'
        self.close()
    def countess(self):
        self.submitted3[str].emit('countess')
        self.close()
    def prince(self):
        self.submitted3[str].emit('prince')
        
        self.close()
    def handmaid(self):
        self.submitted3[str].emit('handmaid')
        self.close()
    def priest(self):
        self.submitted3[str].emit('priest')
        self.close()
    def baron(self):
        self.submitted3[str].emit('baron')
        self.close()
    def guard(self):
        self.submitted3[str].emit('guard')
        self.close()
        

        
        
"""MAIN RUN POINT"""
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWin()
    window.show()
    sys.exit(app.exec_())
