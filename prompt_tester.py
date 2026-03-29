import json
import time
from typing import Dict, List, Any
from llm_helper import llm
from few_shot import FewShotPosts
from post_generator import get_prompt, generate_post
import pandas as pd


class PromptTester:
    """Test and compare different prompt engineering strategies for LinkedIn post generation."""

    def __init__(self, data_source=None):
        self.few_shot = FewShotPosts(custom_df=data_source)
        self.test_results = []

    def test_prompt_strategies(self, topic: str = "Career", length: str = "Medium",
                              language: str = "English", num_tests: int = 3) -> Dict[str, Any]:
        """Test different prompt engineering strategies."""

        strategies = {
            "baseline": self._baseline_prompt,
            "few_shot_2": self._few_shot_2_examples,
            "few_shot_4": self._few_shot_4_examples,
            "detailed_instructions": self._detailed_instructions,
            "chain_of_thought": self._chain_of_thought,
            "style_emphasis": self._style_emphasis
        }

        results = {}

        for strategy_name, strategy_func in strategies.items():
            print(f"🧪 Testing strategy: {strategy_name}")

            strategy_results = []
            for i in range(num_tests):
                try:
                    start_time = time.time()
                    post = strategy_func(topic, length, language)
                    end_time = time.time()

                    metrics = self._evaluate_post(post, topic, length, language)

                    result = {
                        "strategy": strategy_name,
                        "test_run": i + 1,
                        "post": post,
                        "generation_time": round(end_time - start_time, 2),
                        "metrics": metrics,
                        "timestamp": time.time()
                    }

                    strategy_results.append(result)
                    self.test_results.append(result)

                except Exception as e:
                    print(f"❌ Error in {strategy_name} test {i+1}: {str(e)}")
                    continue

            results[strategy_name] = strategy_results

        return results

    def _baseline_prompt(self, topic: str, length: str, language: str) -> str:
        """Basic prompt without examples."""
        length_str = self._get_length_str(length)

        prompt = f'''Generate a LinkedIn post using the below information. No preamble.

1) Topic: {topic}
2) Length: {length_str}
3) Language: {language}
If Language is Hinglish then it means it is a mix of Hindi and English.
The script for the generated post should always be English.'''

        response = llm.invoke(prompt)
        return response.content

    def _few_shot_2_examples(self, topic: str, length: str, language: str) -> str:
        """Standard few-shot with 2 examples."""
        return generate_post(length, language, topic)

    def _few_shot_4_examples(self, topic: str, length: str, language: str) -> str:
        """Few-shot with 4 examples."""
        length_str = self._get_length_str(length)

        prompt = f'''Generate a LinkedIn post using the below information. No preamble.

1) Topic: {topic}
2) Length: {length_str}
3) Language: {language}
If Language is Hinglish then it means it is a mix of Hindi and English.
The script for the generated post should always be English.'''

        examples = self.few_shot.get_filtered_posts(length, language, topic)

        if len(examples) > 0:
            prompt += "4) Use the writing style as per the following examples."

        for i, post in enumerate(examples[:4]):  # Use up to 4 examples
            post_text = post['text']
            prompt += f'\n\n Example {i+1}: \n\n {post_text}'

        response = llm.invoke(prompt)
        return response.content

    def _detailed_instructions(self, topic: str, length: str, language: str) -> str:
        """Detailed instructions with specific guidelines."""
        length_str = self._get_length_str(length)

        prompt = f'''Generate a LinkedIn post using the below information. No preamble.

1) Topic: {topic}
2) Length: {length_str}
3) Language: {language}
If Language is Hinglish then it means it is a mix of Hindi and English.
The script for the generated post should always be English.

4) Writing Guidelines:
   - Start with an engaging hook
   - Include specific examples or stories
   - End with a call-to-action or question
   - Use professional yet conversational tone
   - Include relevant hashtags
   - Make it authentic and valuable'''

        examples = self.few_shot.get_filtered_posts(length, language, topic)

        if len(examples) > 0:
            prompt += "\n\n5) Use the writing style as per the following examples."

        for i, post in enumerate(examples[:2]):
            post_text = post['text']
            prompt += f'\n\n Example {i+1}: \n\n {post_text}'

        response = llm.invoke(prompt)
        return response.content

    def _chain_of_thought(self, topic: str, length: str, language: str) -> str:
        """Chain of thought prompting."""
        length_str = self._get_length_str(length)

        prompt = f'''Generate a LinkedIn post using the below information. No preamble.

1) Topic: {topic}
2) Length: {length_str}
3) Language: {language}
If Language is Hinglish then it means it is a mix of Hindi and English.
The script for the generated post should always be English.

4) Think step by step:
   - First, understand the topic and what value it provides
   - Second, consider what would resonate with LinkedIn audience
   - Third, structure the post with hook, body, and call-to-action
   - Fourth, ensure the tone matches professional networking
   - Finally, write the post following this structure

5) Use the writing style as per the following examples.'''

        examples = self.few_shot.get_filtered_posts(length, language, topic)

        for i, post in enumerate(examples[:2]):
            post_text = post['text']
            prompt += f'\n\n Example {i+1}: \n\n {post_text}'

        response = llm.invoke(prompt)
        return response.content

    def _style_emphasis(self, topic: str, length: str, language: str) -> str:
        """Emphasis on matching writing style."""
        length_str = self._get_length_str(length)

        prompt = f'''Generate a LinkedIn post using the below information. No preamble.

1) Topic: {topic}
2) Length: {length_str}
3) Language: {language}
If Language is Hinglish then it means it is a mix of Hindi and English.
The script for the generated post should always be English.

4) CRITICAL: Match the exact writing style of the examples below:
   - Same level of formality and professionalism
   - Similar sentence structure and length
   - Same use of emojis and hashtags
   - Same tone and voice
   - Same way of engaging the reader

5) Examples to match exactly:'''

        examples = self.few_shot.get_filtered_posts(length, language, topic)

        for i, post in enumerate(examples[:2]):
            post_text = post['text']
            prompt += f'\n\n Example {i+1}: \n\n {post_text}'

        response = llm.invoke(prompt)
        return response.content

    def _get_length_str(self, length: str) -> str:
        """Convert length to descriptive string."""
        if length == "Short":
            return "1 to 5 lines"
        elif length == "Medium":
            return "6 to 10 lines"
        else:  # Long
            return "11 to 15 lines"

    def _evaluate_post(self, post: str, topic: str, length: str, language: str) -> Dict[str, Any]:
        """Evaluate the quality of generated post."""
        lines = post.split('\n')
        word_count = len(post.split())
        char_count = len(post)

        # Basic metrics
        metrics = {
            "word_count": word_count,
            "char_count": char_count,
            "line_count": len(lines),
            "has_emoji": any(char in post for char in ['🚀', '💼', '📈', '🎯', '💪', '📚', '🤝', '🌟', '🔥', '✨']),
            "has_hashtag": '#' in post,
            "has_question": '?' in post,
            "topic_relevance": topic.lower() in post.lower(),
            "language_match": language.lower() in post.lower() or language == "English"
        }

        # Length appropriateness
        if length == "Short":
            metrics["length_appropriate"] = 10 <= word_count <= 50
        elif length == "Medium":
            metrics["length_appropriate"] = 50 <= word_count <= 120
        else:  # Long
            metrics["length_appropriate"] = 120 <= word_count <= 200

        return metrics

    def compare_strategies(self, results: Dict[str, List]) -> pd.DataFrame:
        """Compare different strategies and return summary."""
        summary_data = []

        for strategy, tests in results.items():
            if not tests:
                continue

            avg_time = sum(test['generation_time'] for test in tests) / len(tests)
            avg_words = sum(test['metrics']['word_count'] for test in tests) / len(tests)
            avg_length_appropriate = sum(test['metrics']['length_appropriate'] for test in tests) / len(tests)
            avg_has_emoji = sum(test['metrics']['has_emoji'] for test in tests) / len(tests)
            avg_has_hashtag = sum(test['metrics']['has_hashtag'] for test in tests) / len(tests)
            avg_topic_relevance = sum(test['metrics']['topic_relevance'] for test in tests) / len(tests)

            summary_data.append({
                "Strategy": strategy,
                "Avg Generation Time (s)": round(avg_time, 2),
                "Avg Word Count": round(avg_words, 1),
                "Length Appropriate %": round(avg_length_appropriate * 100, 1),
                "Emoji Usage %": round(avg_has_emoji * 100, 1),
                "Hashtag Usage %": round(avg_has_hashtag * 100, 1),
                "Topic Relevance %": round(avg_topic_relevance * 100, 1),
                "Total Tests": len(tests)
            })

        return pd.DataFrame(summary_data)

    def save_results(self, filename: str = "prompt_test_results.json"):
        """Save test results to JSON file."""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.test_results, f, indent=4, ensure_ascii=False)
        print(f"✅ Results saved to {filename}")

    def load_results(self, filename: str = "prompt_test_results.json"):
        """Load previous test results."""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                self.test_results = json.load(f)
            print(f"✅ Loaded {len(self.test_results)} test results")
        except FileNotFoundError:
            print("❌ No previous results found")


if __name__ == "__main__":
    # Example usage
    tester = PromptTester()

    print("🚀 Starting prompt engineering tests...")
    print("Testing different strategies for Career/Medium/English posts...")

    # Run tests
    results = tester.test_prompt_strategies(
        topic="Career",
        length="Medium",
        language="English",
        num_tests=2  # Quick test, increase for more thorough testing
    )

    # Compare strategies
    comparison = tester.compare_strategies(results)
    print("\n📊 Strategy Comparison:")
    print(comparison.to_string(index=False))

    # Save results
    tester.save_results()

    print("\n✅ Testing complete! Check prompt_test_results.json for detailed results.")