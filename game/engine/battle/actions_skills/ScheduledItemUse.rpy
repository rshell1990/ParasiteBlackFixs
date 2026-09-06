init python:
    class Battle_ScheduledItemUse:
        def __init__(self,
                SourceAction = None,

                # battlechar, list of battlechars or any enum entry from BATTLE_TARGETS
                UseTarget = None,

                Effects_OnTarget = [],
                Effects_OnSelf = [],

                GenericLogLine = True,

                SoundUse_CustomList = None,
                SoundImpact_CustomList = None,  # if not none, sound to play on target char
                
                CharSkinAnimToPlay = None,      # if not none, char skin anim ID to override "cast"
                TargetVFXID = None,             # if not none, spawn this vfx ID on use target
                ):
            self.ItemName = SourceAction.ItemName
            self.ItemID = SourceAction.ItemID
            self.UserBattleChar = SourceAction.Owner_BattleChar

            self.TargetList = Battle_ProcessTargetList(self.UserBattleChar, UseTarget)

            self.Effects_OnTarget = Effects_OnTarget
            self.Effects_OnSelf = Effects_OnSelf

            self.GenericLogLine = GenericLogLine

            self.SoundUse_CustomList = SoundUse_CustomList
            self.SoundImpact_CustomList = SoundImpact_CustomList

            self.CustomLogLine = None

            self.CharSkinAnimToPlay = CharSkinAnimToPlay
            self.TargetVFXID = TargetVFXID

            BattleScene.ScheduledAttackQueue.insert(0, self)

        def ExecuteAction(self):
            for BattleChar in reversed(self.TargetList):
                if not BattleChar.IsAlive:
                    self.TargetList.remove(BattleChar)

            if len(self.TargetList) == 0:
                return

            if self.CharSkinAnimToPlay is not None:
                PlayedAnim = Battle_RunCharAnim(self.UserBattleChar, self.CharSkinAnimToPlay)
            else:
                PlayedAnim = Battle_RunCharAnim(self.UserBattleChar, "cast")

            if self.SoundUse_CustomList:
                Battle_PlaySoundOnBattleChar(renpy.random.choice(self.SoundUse_CustomList), self.UserBattleChar)
            else:
                Battle_PlaySoundOnBattleChar(renpy.random.choice(soundLib["BattleSkill_Defend_Use"]), self.UserBattleChar)

            Battle_RemoveItem(self.UserBattleChar, self.ItemID)
            Battle_LoopStep(PlayedAnim.Warmup)

            for Target in self.TargetList:
                if self.TargetVFXID:
                    Battle_SpawnVfxOnChar(Target, self.TargetVFXID)
                if self.SoundImpact_CustomList:
                    Battle_PlaySoundOnBattleChar(renpy.random.choice(self.SoundImpact_CustomList), Target)
                for OnHitEffect in self.Effects_OnTarget:
                    OnHitEffect.ApplyEffect(Target)
            for OnSelfEffect in self.Effects_OnSelf:
                OnSelfEffect.ApplyEffect(self.UserBattleChar)

            if self.GenericLogLine:
                Battle_AddLogEntry_Autoformat(
                    USER = self.UserBattleChar,
                    ITEM_NAME = self.ItemName,
                    String = tra(_("USER_NAME uses ITEM_NAME!")))

            Battle_LoopStep(PlayedAnim.Cooldown)
            return

    def Battle_RemoveItem(User, ItemID):
        BattleSide = User.BattleSide
        RemItemFrom(BattleScene.ItemPools[BattleSide], ItemID)
        if ItemID not in BattleScene.ItemsRemovedDuringBattle[BattleSide]:
            BattleScene.ItemsRemovedDuringBattle[BattleSide][ItemID] = 1
        else:
            BattleScene.ItemsRemovedDuringBattle[BattleSide][ItemID] += 1
        return

    # this checks recovery mod and clamps
    # added for log lines might be useful for sth else
    def Battle_GetHealthRecoveredModifiedAndClamped(Char, Value):
        return min(round(Battle_GetHealthRecoveryMod(Char) * Value), Char.HealthMax - Char.Health)
    def Battle_GetEnergyRecoveredModifiedAndClamped(Char, Value):
        return min(round(Battle_GetEnergyRecoveryMod(Char) * Value), Char.EnergyMax - Char.Energy)