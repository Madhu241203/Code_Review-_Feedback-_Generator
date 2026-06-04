import json
import ollama


def review_code(code):

    prompt = f"""
You are an expert code reviewer.

Analyze the following code without executing it.

Return ONLY a valid JSON object with these keys:

identified_issues
improvement_suggestions
code_quality_level
review_summary

Code:

{code}
"""

    response = ollama.chat(
        model="llama3",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    result = response["message"]["content"]

    try:
        start = result.find("{")
        end = result.rfind("}") + 1

        if start != -1 and end != -1:
            result = result[start:end]

        return json.loads(result)

    except Exception:
        return {
            "identified_issues": ["Could not parse model response"],
            "improvement_suggestions": [],
            "code_quality_level": "Unknown",
            "review_summary": result
        }