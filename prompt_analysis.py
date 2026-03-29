import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
import numpy as np


class PromptAnalysis:
    """Analyze and visualize prompt testing results."""

    def __init__(self, results_file: str = "prompt_test_results.json"):
        self.results_file = results_file
        self.df = None
        self.load_data()

    def load_data(self):
        """Load and process test results."""
        try:
            with open(self.results_file, 'r', encoding='utf-8') as f:
                data = json.load(f)

            self.df = pd.DataFrame(data)

            # Flatten metrics
            metrics_df = pd.json_normalize(self.df['metrics'])
            self.df = pd.concat([self.df.drop('metrics', axis=1), metrics_df], axis=1)

            print(f"✅ Loaded {len(self.df)} test results")
            print(f"📊 Strategies tested: {self.df['strategy'].nunique()}")
            print(f"🧪 Total test runs: {len(self.df)}")

        except FileNotFoundError:
            print("❌ Results file not found. Run prompt_tester.py first.")

    def create_summary_report(self):
        """Create a comprehensive summary report."""
        if self.df is None:
            return

        print("\n" + "="*80)
        print("📊 PROMPT ENGINEERING ANALYSIS REPORT")
        print("="*80)

        # Overall statistics
        print("\n🎯 OVERALL STATISTICS:")
        print(f"   Total tests: {len(self.df)}")
        print(f"   Average generation time: {self.df['generation_time'].mean():.2f}s")
        print(f"   Average word count: {self.df['word_count'].mean():.1f}")
        print(f"   Length appropriateness: {(self.df['length_appropriate'].mean() * 100):.1f}%")
        print(f"   Emoji usage rate: {(self.df['has_emoji'].mean() * 100):.1f}%")
        print(f"   Hashtag usage rate: {(self.df['has_hashtag'].mean() * 100):.1f}%")
        print(f"   Topic relevance: {(self.df['topic_relevance'].mean() * 100):.1f}%")
        # Strategy comparison
        print("\n📈 STRATEGY PERFORMANCE:")
        strategy_stats = self.df.groupby('strategy').agg({
            'generation_time': ['mean', 'std'],
            'word_count': ['mean', 'std'],
            'length_appropriate': 'mean',
            'has_emoji': 'mean',
            'has_hashtag': 'mean',
            'topic_relevance': 'mean'
        }).round(3)

        strategy_stats.columns = ['avg_time', 'time_std', 'avg_words', 'words_std',
                                'length_acc', 'emoji_rate', 'hashtag_rate', 'topic_acc']

        for strategy in strategy_stats.index:
            stats = strategy_stats.loc[strategy]
            print(f"\n   {strategy.upper()}:")
            print(f"      ⏱️  Avg Time: {stats['avg_time']:.2f}s")
            print(f"      📝 Avg Words: {stats['avg_words']:.1f}")
            print(f"      📏 Length OK: {stats['length_acc']:.1%}")
            print(f"      😊 Emoji Rate: {stats['emoji_rate']:.1%}")
            print(f"      #️⃣  Hashtag Rate: {stats['hashtag_rate']:.1%}")
            print(f"      🎯 Topic Acc: {stats['topic_acc']:.1%}")

        # Best performers
        print("\n🏆 BEST PERFORMERS:")
        best_time = self.df.loc[self.df['generation_time'].idxmin()]
        best_quality = self.df.loc[(self.df['length_appropriate'] &
                                   self.df['topic_relevance'] &
                                   self.df['has_emoji'] &
                                   self.df['has_hashtag']).idxmax()]

        print(f"   ⚡ Fastest generation: {best_time['strategy']} ({best_time['generation_time']:.2f}s)")
        print(f"   🎯 Best quality: {best_quality['strategy']} (all metrics perfect)")

        # Insights
        print("\n💡 KEY INSIGHTS:")        # Time vs quality trade-off
        corr_time_quality = self.df['generation_time'].corr(
            self.df[['length_appropriate', 'has_emoji', 'has_hashtag']].mean(axis=1)
        )
        print(f"   ⚖️  Time-Quality Correlation: {corr_time_quality:.3f}")

        # Most consistent strategy
        most_consistent = self.df.groupby('strategy')['generation_time'].std().idxmin()
        print(f"   🎲 Most consistent timing: {most_consistent}")

        # Strategy recommendations
        print("\n🎯 RECOMMENDATIONS:")
        if strategy_stats.loc['style_emphasis', 'emoji_rate'] > 0.5:
            print("   ✅ 'style_emphasis' excels at including emojis and hashtags")
        if strategy_stats.loc['detailed_instructions', 'hashtag_rate'] > 0.5:
            print("   ✅ 'detailed_instructions' is great for hashtag usage")
        if strategy_stats.loc['baseline', 'avg_time'] < strategy_stats['avg_time'].mean():
            print("   ✅ 'baseline' is fastest but lacks engagement features")

    def create_visualizations(self):
        """Create and save performance visualizations."""
        if self.df is None:
            return

        # Set up the plotting style
        plt.style.use('default')
        sns.set_palette("husl")

        # Create figure with subplots
        fig, axes = plt.subplots(2, 3, figsize=(15, 10))
        fig.suptitle('Prompt Engineering Strategy Analysis', fontsize=16, fontweight='bold')

        # 1. Generation Time Comparison
        strategy_order = self.df.groupby('strategy')['generation_time'].mean().sort_values().index
        sns.barplot(data=self.df, x='strategy', y='generation_time', order=strategy_order, ax=axes[0,0])
        axes[0,0].set_title('Average Generation Time (seconds)')
        axes[0,0].set_ylabel('Time (s)')
        axes[0,0].tick_params(axis='x', rotation=45)

        # 2. Word Count Distribution
        sns.boxplot(data=self.df, x='strategy', y='word_count', order=strategy_order, ax=axes[0,1])
        axes[0,1].set_title('Word Count Distribution')
        axes[0,1].set_ylabel('Word Count')
        axes[0,1].tick_params(axis='x', rotation=45)

        # 3. Quality Metrics
        quality_metrics = ['length_appropriate', 'has_emoji', 'has_hashtag', 'topic_relevance']
        quality_data = self.df.groupby('strategy')[quality_metrics].mean().reset_index()
        quality_data_melted = quality_data.melt(id_vars='strategy', var_name='metric', value_name='rate')

        sns.barplot(data=quality_data_melted, x='strategy', y='rate', hue='metric', ax=axes[0,2])
        axes[0,2].set_title('Quality Metrics Success Rate')
        axes[0,2].set_ylabel('Success Rate')
        axes[0,2].legend(title='Metric', bbox_to_anchor=(1.05, 1), loc='upper left')
        axes[0,2].tick_params(axis='x', rotation=45)

        # 4. Time vs Quality Scatter
        avg_by_strategy = self.df.groupby('strategy').agg({
            'generation_time': 'mean',
            'length_appropriate': 'mean',
            'has_emoji': 'mean',
            'has_hashtag': 'mean'
        }).reset_index()

        quality_score = avg_by_strategy[['length_appropriate', 'has_emoji', 'has_hashtag']].mean(axis=1)

        sns.scatterplot(data=avg_by_strategy, x='generation_time', y=quality_score,
                       hue='strategy', s=100, ax=axes[1,0])
        axes[1,0].set_title('Time vs Quality Trade-off')
        axes[1,0].set_xlabel('Generation Time (s)')
        axes[1,0].set_ylabel('Quality Score')
        axes[1,0].legend(bbox_to_anchor=(1.05, 1), loc='upper left')

        # 5. Strategy Performance Radar
        from math import pi
        categories = ['Speed', 'Quality', 'Engagement', 'Consistency']
        fig_radar, ax_radar = plt.subplots(figsize=(6, 6), subplot_kw=dict(projection='polar'))

        # Calculate scores for each strategy
        radar_data = {}
        for strategy in self.df['strategy'].unique():
            strategy_data = self.df[self.df['strategy'] == strategy]

            speed_score = 1 / (1 + strategy_data['generation_time'].mean())  # Normalize speed
            quality_score = strategy_data[['length_appropriate', 'topic_relevance']].mean().mean()
            engagement_score = strategy_data[['has_emoji', 'has_hashtag']].mean().mean()
            consistency_score = 1 / (1 + strategy_data['generation_time'].std())  # Lower std = higher consistency

            radar_data[strategy] = [speed_score, quality_score, engagement_score, consistency_score]

        # Plot radar for each strategy
        angles = [n / float(len(categories)) * 2 * pi for n in range(len(categories))]
        angles += angles[:1]

        for strategy, values in radar_data.items():
            values += values[:1]
            ax_radar.plot(angles, values, 'o-', linewidth=2, label=strategy)
            ax_radar.fill(angles, values, alpha=0.25)

        ax_radar.set_xticks(angles[:-1])
        ax_radar.set_xticklabels(categories)
        ax_radar.set_ylim(0, 1)
        ax_radar.set_title('Strategy Performance Radar', size=16, fontweight='bold', pad=20)
        ax_radar.legend(loc='upper right', bbox_to_anchor=(1.2, 1.0))
        ax_radar.grid(True)

        # Save radar plot separately
        fig_radar.savefig('prompt_strategy_radar.png', dpi=300, bbox_inches='tight')
        plt.close(fig_radar)

        # 6. Sample Post Comparison
        axes[1,1].axis('off')
        axes[1,1].text(0.1, 0.9, 'Sample Generated Posts:', fontsize=12, fontweight='bold')

        sample_posts = {}
        for strategy in self.df['strategy'].unique():
            sample = self.df[self.df['strategy'] == strategy]['post'].iloc[0][:200] + "..."
            sample_posts[strategy] = sample

        y_pos = 0.8
        for strategy, post in sample_posts.items():
            axes[1,1].text(0.1, y_pos, f"{strategy.upper()}:", fontsize=10, fontweight='bold')
            axes[1,1].text(0.15, y_pos-0.05, post, fontsize=8, wrap=True)
            y_pos -= 0.15

        axes[1,1].set_title('Sample Output Comparison')

        # 7. Performance Summary Table
        axes[1,2].axis('off')
        summary_data = self.df.groupby('strategy').agg({
            'generation_time': 'mean',
            'word_count': 'mean',
            'length_appropriate': 'mean',
            'has_emoji': 'mean',
            'has_hashtag': 'mean'
        }).round(2)

        table_data = []
        for strategy in summary_data.index:
            row = summary_data.loc[strategy]
            table_data.append([
                strategy,
                ".2f"                ".0f"                ".0%"                ".0%"                ".0%"
            ])

        table = axes[1,2].table(cellText=table_data,
                               colLabels=['Strategy', 'Time(s)', 'Words', 'Length OK', 'Emoji', 'Hashtag'],
                               loc='center',
                               cellLoc='center')
        table.auto_set_font_size(False)
        table.set_fontsize(8)
        table.scale(1, 1.5)
        axes[1,2].set_title('Performance Summary Table')

        plt.tight_layout()
        plt.savefig('prompt_analysis_visualization.png', dpi=300, bbox_inches='tight')
        plt.close()

        print("✅ Visualizations saved as 'prompt_analysis_visualization.png'")
        print("✅ Radar chart saved as 'prompt_strategy_radar.png'")

    def export_detailed_report(self, filename: str = "prompt_analysis_report.md"):
        """Export detailed analysis report to markdown."""
        if self.df is None:
            return

        report = f"""# Prompt Engineering Analysis Report

## Executive Summary

This report analyzes the performance of {len(self.df['strategy'].unique())} different prompt engineering strategies for LinkedIn post generation using Groq's Llama 3.3 70B model.

**Test Parameters:**
- Topic: Career
- Length: Medium (6-10 lines)
- Language: English
- Tests per strategy: {len(self.df) // len(self.df['strategy'].unique())}

## Performance Overview

### Key Metrics
- **Total Tests:** {len(self.df)}
- **Average Generation Time:** {self.df['generation_time'].mean():.2f}s
- **Average Word Count:** {self.df['word_count'].mean():.0f}
- **Quality Score:** {(self.df[['length_appropriate', 'has_emoji', 'has_hashtag']].mean().mean() * 100):.1f}%

### Strategy Rankings

{self.df.groupby('strategy').agg({
    'generation_time': 'mean',
    'word_count': 'mean',
    'length_appropriate': 'mean',
    'has_emoji': 'mean',
    'has_hashtag': 'mean'
}).round(2).to_markdown()}

## Detailed Results

"""

        for strategy in self.df['strategy'].unique():
            strategy_data = self.df[self.df['strategy'] == strategy]
            report += f"""### {strategy.upper()} Strategy

**Performance Metrics:**
- Average Time: {strategy_data['generation_time'].mean():.2f}s
- Word Count: {strategy_data['word_count'].mean():.0f}
- Length Appropriate: {(strategy_data['length_appropriate'].mean() * 100):.0f}%
- Emoji Usage: {(strategy_data['has_emoji'].mean() * 100):.0f}%
- Hashtag Usage: {(strategy_data['has_hashtag'].mean() * 100):.0f}%

**Sample Output:**
{strategy_data['post'].iloc[0][:300]}...

---
"""

        with open(filename, 'w', encoding='utf-8') as f:
            f.write(report)

        print(f"✅ Detailed report saved as '{filename}'")


if __name__ == "__main__":
    analyzer = PromptAnalysis()

    # Generate comprehensive report
    analyzer.create_summary_report()
    analyzer.create_visualizations()
    analyzer.export_detailed_report()

    print("\n🎉 Analysis complete! Check the generated files:")
    print("   📊 prompt_analysis_visualization.png")
    print("   📈 prompt_strategy_radar.png")
    print("   📋 prompt_analysis_report.md")