from Assets.card import Card

TEST_SUIT = "SPADES"

BLACKJACK_HAND = [Card(TEST_SUIT,"ACE",0,True), Card(TEST_SUIT,"KING",0,True)]

SIXTEEN_HAND = [Card(TEST_SUIT,"6",0,True), Card(TEST_SUIT,"KING",0,True)]

SEVENTEEN_HAND = [Card(TEST_SUIT,"6",0,True), Card(TEST_SUIT,"KING",0,True), Card(TEST_SUIT,"1",0,True)]

EIGHTEEN_HAND = [Card(TEST_SUIT,"5",0,True), Card(TEST_SUIT,"KING",0,True), Card(TEST_SUIT,"1",0,True), Card(TEST_SUIT,"2",0,True)]

DEALER_EIGHTEEN_HAND = [Card(TEST_SUIT,"5",0,True), Card(TEST_SUIT,"ACE",0,True), Card(TEST_SUIT,"2",0,True)]

TWENTYONE_NO_BLACKJACK_HAND = [Card(TEST_SUIT,"5",0,True), Card(TEST_SUIT,"KING",0,True), Card(TEST_SUIT,"1",0,True), Card(TEST_SUIT,"5",0,True)]

BUST_HAND = [Card(TEST_SUIT,"5",0,True), Card(TEST_SUIT,"KING",0,True), Card(TEST_SUIT,"JACK",0,True)]