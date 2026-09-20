init python:
    # lighter version of sched.attack: meant to be used 
    # for quick implementing of stuff like "put status effect on ally"
    # main differences are, it avoids the whole targeting AR/DR stuff
    # and it avoids damage calc (does no damage by itself at all)
    class Battle_ScheduledCast:
        def __init__(self, 
                SourceSkillObj = None,

                # battlechar, list of battlechars or any enum entry from BATTLE_TARGETS
                CastTarget = None,

                Effects_OnTarget = None,
                Effects_OnSelf = None,
                GenericLogLine = True,
                PlayCharSkinUseSkillSound = True,

                SoundUse_CustomList = None,    # if not none, sounds to play on cast
                SoundImpact_CustomList = None, # if not none, sounds to play on target char
                SoundImpact_OneShotList = None, # same as above, but only played once (to not earrape with *targets)

                TargetVFXID = None # if not none, spawn this vfx ID on cast target
                ):

            self.SkillName = SourceSkillObj.DisplayName if SourceSkillObj else ""
            self.UserBattleChar = SourceSkillObj.Owner_BattleChar if SourceSkillObj else None

            self.TargetList = Battle_ProcessTargetList(self.UserBattleChar, CastTarget)

            self.Effects_OnTarget = Effects_OnTarget if Effects_OnTarget is not None else []
            self.Effects_OnSelf = Effects_OnSelf if Effects_OnSelf is not None else []

            self.GenericLogLine = GenericLogLine

            self.PlayCharSkinUseSkillSound = PlayCharSkinUseSkillSound

            self.SoundUse_CustomList = SoundUse_CustomList
            self.SoundImpact_CustomList = SoundImpact_CustomList
            self.SoundImpact_OneShotList = SoundImpact_OneShotList

            self.TargetVFXID = TargetVFXID

            BattleScene.ScheduledAttackQueue.insert(0, self)

        def ExecuteAction(self):
            # Filter out dead characters safely without mutating list in-place
            self.TargetList = [char for char in self.TargetList if getattr(char, "IsAlive", True)]

            if not self.TargetList:
                return

            PlayedAnim = Battle_RunCharAnim(self.UserBattleChar, "cast")

            if self.PlayCharSkinUseSkillSound:
                Battle_PlayCharSkinSound("Char_UseSkill", self.UserBattleChar, Voice = True, Chance = 0.25)
            
            if self.SoundUse_CustomList:
                Battle_PlaySoundOnBattleChar(renpy.random.choice(self.SoundUse_CustomList), self.UserBattleChar)
            elif "BattleSkill_Defend_Use" in soundLib:
                Battle_PlaySoundOnBattleChar(renpy.random.choice(soundLib["BattleSkill_Defend_Use"]), self.UserBattleChar)

            Battle_LoopStep(PlayedAnim.Warmup)

            if self.SoundImpact_OneShotList:
                Battle_PlaySoundOnBattleChar(renpy.random.choice(self.SoundImpact_OneShotList), self.TargetList[0])

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
                    SKILL_NAME = self.SkillName,
                    String = _("USER_NAME uses SKILL_NAME!"))

            Battle_LoopStep(PlayedAnim.Cooldown)
            return