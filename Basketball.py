import random
import argparse

class BasketballPlayer:
    def __init__(self, name, games_played, total_points, points_last_season):
        self.name = name
        self.games_played = games_played
        self.total_points = total_points
        self.points_last_season = points_last_season
        self.point_average = self.calculate_point_average()

    def calculate_point_average(self):
        """Calculate average points per game."""
        return self.total_points / self.games_played if self.games_played > 0 else 0

    def predict_average_for_season(self):
        """Predict average points for the season based on past performance."""
        growth_factor = self.estimate_growth_factor()
        return self.point_average * growth_factor

    def estimate_growth_factor(self):
        """Estimate growth factor based on player trends."""
        if self.points_last_season > 1000:
            return random.uniform(1.05, 1.15)
        else:
            return random.uniform(0.95, 1.05)

    def predict_injury_risk(self, risk_threshold=20):
        """
        Predict injury risk based on point average.

        Args:
            risk_threshold (int): Average points threshold above which risk increases.
        """
        risk = "High" if self.point_average > risk_threshold else "Low"
        return f"{self.name}: {risk} injury risk based on point average."

    def __str__(self):
        return f"{self.name}: Current Avg = {self.point_average:.2f}, Predicted Avg = {self.predict_average_for_season():.2f}"

if __name__ == "__main__":
    player1 = BasketballPlayer("Ibrahim Sesay", 51, 1300, 1040)
    player2 = BasketballPlayer("Abdoullah S", 49, 980, 830)

    print(player1)
    print("Calculated Avg:", player1.calculate_point_average())
    print("Predicted Avg:", player1.predict_average_for_season())
    print(player1.predict_injury_risk())

    print(player2)
    print("Calculated Avg:", player2.calculate_point_average())
    print("Predicted Avg:", player2.predict_average_for_season())
    print(player2.predict_injury_risk())

    # Simple test checks
    assert player1.calculate_point_average() == 1300 / 51
    assert player2.calculate_point_average() == 980 / 49
