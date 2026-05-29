"""Analyze keyword search trends by region using Google Trends data."""

import matplotlib.pyplot as plt
from pytrends.request import TrendReq


def analyze_keyword_trends(keyword: str = "Data Science") -> None:
    """Fetch and plot regional interest for a given keyword."""
    try:
        trends = TrendReq()
        trends.build_payload(kw_list=[keyword])
        data = trends.interest_by_region()

        if data.empty:
            print(f"No trend data available for '{keyword}'.")
            return

        print(data.sample(10))

        # Plot the top 15 regions
        sample = data.sample(min(15, len(data)))
        sample.reset_index().plot(
            x="geoName",
            y=keyword,
            figsize=(12, 8),
            kind="bar",
        )
        plt.title(f"Regional Interest in '{keyword}'")
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"Error fetching trend data: {e}")


if __name__ == "__main__":
    analyze_keyword_trends("Data Science")
