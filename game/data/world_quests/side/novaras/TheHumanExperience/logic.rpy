init python:
    @AppendToAllQuests
    class QstHumanExp(BaseQuest):        
        TITLE = _("The Human Experience")
        DESCRIPTION = _("Now that I have found a place for Myu to stay, I've gotta make sure she 'settles in' alright...")
        GOALS = {
                0: QuestStage(_("Check up on Myu"),
                    trackTag = "btn_azul_safehouse",
                    hintTxt = _("I should check up on Myu another day, see if she is alright.")),
                1: QuestStage(_("Feed Myu"),
                    trackTag = "btn_novaras_market_stalls",
                    hintTxt = _("Myu's appetites grow. Wonder if I can handle supplying her further... Butcher at the market should have more meat I can bring her.")),
                2: QuestStage(_("Teach Myu some Alderian"),
                    trackTag = "btn_azul_safehouse",
                    hintTxt = _("Myu wants 'words'. A slimelark that speaks... This is going to be interesting.")),
                3: QuestStage(_("Grab a book on Alderian language"),
                    trackTag = "btn_novaras_library",
                    hintTxt = _("Perhaps I can speed up teaching Myu if I can find a book on Alderian language. I should try Novaras Library.")),
                4: QuestStage(_("Bring the books collection to Myu"),
                    trackTag = "btn_azul_safehouse",
                    hintTxt = _("I feel like I've just bought half the library out. Hope these books will help Myu learn to speak.")),
                5: QuestStage(_("Let Myu study"),
                    trackTag = "btn_azul_safehouse",
                    hintTxt = _("I gave Myu a huge collection of books on Alderian language. I should leave her alone to study for now, maybe check up on her later.")),
                6: QuestStage(_("Give Myu a tour of the city"),
                    trackTag = "btn_azul_safehouse",
                    hintTxt = _("We're walking a thin line here. Myu is eager to see 'the world outside', but the world outside will attack her on sight. I hope this works out...")),
                7: QuestStage(_("Let Myu rest"),
                    trackTag = "btn_azul_safehouse",
                    hintTxt = _("Myu was excited to see the city. I should check up on her once she processes all the excitement.")),
                8: QuestStage(_("Get better food"),
                    trackTag = "btn_novaras_tavern",
                    hintTxt = _("Myu doesn't feel right. Maybe some fresh food from the Iron Unicorn tavern can improve her condition?")),
                9: QuestStage(_("Learn more about slimelarks"),
                    trackTag = "btn_novaras_library",
                    hintTxt = _("Myu doesn't feel right... at all! I need to learn about slimelarks. The library could be of use.")),
                10: QuestStage(_("Collect wildflowers"),
                    hintTxt = _("It seems that slimelarks' diet is not exclusively carnivorous. I need to gather some wildflowers at the Balun lake.")),
                11: QuestStage(_("Bring Myu the wildflowers"),
                    trackTag = "btn_azul_safehouse",
                    hintTxt = _("I have gathered some wildflowers. Really hope this helps Myu get better... Time to go bring them over now.")),
                12: QuestStage(_("Take Myu out 'hunting'"),
                    trackTag = "btn_azul_safehouse",
                    hintTxt = _("Myu needs meat to survive. And not the steak kind. I should take her out on the 'hunt' one night.")),
            }

        def __init__(self):
            super().__init__()

            self.XpReward = 500
            self.checkUp = False
            self.haggledForBooks = False
            self.booksPrice = 500
            self.valaRevisit = False
            self.myuSpeaksDay = -1
            self.buttGrab = False
            self.checkUpAfterTour = False

        def onEnter(self):  
            if GetLocID() in ["azul_safehouse", "azul_safehouse_bedroom"]:
                if self.progress == 0:
                    if self.checkUp:
                        return TriggeredEvent("qst_HumanExp_0_checkup")
                elif self.progress == 7:
                    if self.checkUpAfterTour:
                        return TriggeredEvent("qst_HumanExp_7_checkupAfterTour")
                elif self.progress == 11:
                    return TriggeredEvent("qst_HumanExp_11_returnFlowers")

        def onMidnight(self):
            if self.progress == 0:
                self.checkUp = True
            elif self.progress == 5:
                if GetGameDay() >= self.myuSpeaksDay:
                    DialogueMyu().myuKnowsLang = True
            elif self.progress == 7:
                self.checkUpAfterTour = True

        def extraDialogue(self):
            if self.progress == 1:
                if PlayerItemQty("red_meat") > 0:
                    yield ("myu_root", DNode(_("Here, Myu, some food."), "qst_HumanExp_1_feedMyuDialogue"))
            elif self.progress == 2:
                yield ("myu_root", DNode(_("Let's start with the lesson."), "qst_HumanExp_2_lesson"))
            elif self.progress == 3:
                if self.valaRevisit:
                    yield ("vala_root", DNode(_("About these books on Alderian..."), "qst_HumanExp_3_grabBook_atLibrary_revisit"))
                else:
                    yield ("vala_root", DNode(_("Do you have any books that help teach Alderian?"), "qst_HumanExp_3_grabBook_atLibrary"))
            elif self.progress == 4:
                if PlayerItemQty("qst_myu_books") > 0:
                    yield ("myu_root", DNode(_("Give her the books collection."), "qst_HumanExp_3_grabBook_returnBooks"))
            elif self.progress == 5:
                if DialogueMyu().myuKnowsLang:
                    yield ("myu_root", DNode(_("How is your Alderian?"), "qst_HumanExp_5_checkIn_speaks"))
                else:
                    yield ("myu_root", DNode(_("How is your Alderian?"), "qst_HumanExp_5_checkIn_early"))
            elif self.progress == 6:
                yield ("myu_root", DNode(_("{image=[ICON.CLOCK]} I'm ready to take you on tour now, Myu."), "qst_HumanExp_6_cityTour"))
            elif self.progress == 8:
                yield ("shay_root", DNode(_("I was hoping to get some food..."), "qst_HumanExp_8_shayGetBetterFood"))
            elif self.progress == 9:
                yield ("vala_root", DNode(_("Ask for a book about Slimelarks."), "qst_HumanExp_9_valaLearnSlimelarks"))
            elif self.progress == 12:
                if not IsDaytime():
                    yield ("myu_root", DNode(_("Come on Myu... It's time to take you hunting."), "qst_HumanExp_12_goHunting"))

        def onComplete(self):
            QstStart(PrimerQstNewMyu)
            return

        def onStart(self):
            wLocs["azul_safehouse"].displayName = STR_LOC.NOV_MYU_HIDEOUT
            wLocs["azul_safehouse_bedroom"].displayName = STR_LOC.NOV_MYU_HIDEOUT_BEDROOM
            return