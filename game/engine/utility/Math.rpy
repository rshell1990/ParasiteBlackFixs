# math.rpy - Math and Utility Functions for Ren'Py
init python:
    import random
    import math

    # Basic Utility Functions

    def Clamp(val, min_val, max_val):
        """Clamp a value between a minimum and a maximum limit."""
        return max(min_val, min(val, max_val))

    ClampValue = Clamp

    def Lerp(a, b, t):
        """Linear interpolation between 'a' and 'b' by percentage 't' (0.0 to 1.0)."""
        return a + (b - a) * Clamp(t, 0.0, 1.0)

    def Remap(val, in_min, in_max, out_min, out_max):
        """Map a value from one range to another range."""
        if in_min == in_max:
            return out_min
        normalized = (val - in_min) / float(in_max - in_min)
        return out_min + normalized * (out_max - out_min)


    # RNG & Chance Functions

    def Chance(percent):
        """
        Returns True based on a percentage chance (0 to 100).
        Example: Chance(25) returns True 25% of the time.
        """
        return renpy.random.randint(1, 100) <= percent

    def RollDice(sides=6, amount=1, bonus=0):
        """
        Simulates rolling tabletop dice.
        Example: RollDice(6, 2, 3) rolls 2d6 + 3.
        """
        total = sum(renpy.random.randint(1, sides) for _ in range(amount))
        return total + bonus

    def WeightedChoice(choices):
        """
        Selects a random item based on numerical weights.
        
        Usage:
            loot = WeightedChoice({
                "Gold": 50,      # 50% weight
                "Iron Sword": 30,# 30% weight
                "Healing Potion": 20 # 20% weight
            })
        """
        total_weight = sum(choices.values())
        roll = renpy.random.uniform(0, total_weight)
        cumulative = 0.0
        for item, weight in choices.items():
            cumulative += weight
            if roll <= cumulative:
                return item
        return list(choices.keys())[-1]


    # Stats & Progression Math

    def ApplyVariance(value, percent_variance=10):
        """
        Applies a random +/- percentage variance to a base number (useful for damage).
        Example: ApplyVariance(100, 10) returns a number between 90 and 110.
        """
        factor = percent_variance / 100.0
        min_val = value * (1.0 - factor)
        max_val = value * (1.0 + factor)
        return round(renpy.random.uniform(min_val, max_val))

    def CalculateXpForLevel(level, base_xp=100, exponent=1.5):
        """Calculates total required XP for a given level using an exponential curve."""
        return int(base_xp * (level ** exponent))