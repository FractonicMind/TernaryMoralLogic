# Clarifying Question Engine

## Overview

The Clarifying Question Engine generates contextually appropriate questions when Sacred Pause is triggered, helping humans provide guidance for morally complex scenarios. The system uses a three-layered fallback strategy to ensure relevant, clear questions regardless of domain.

## Three-Layered Architecture

### Layer 1: Custom Domain Templates (Primary)

Pre-crafted questions for known scenarios provide the highest quality responses.

```python
DOMAIN_TEMPLATES = {
    'medical_ethics': {
        'resource_allocation': [
            "Which factors should be prioritized: immediate need, likelihood of success, or long-term benefit?",
            "Should we consider the patient's quality of life or focus solely on life extension?",
            "How should we balance individual patient needs against population health concerns?"
        ],
        'consent_issues': [
            "Is the patient capable of providing informed consent at this time?",
            "Should family preferences override documented patient wishes?",
            "What level of risk disclosure is appropriate for this patient's condition?"
        ],
        'end_of_life': [
            "Is the focus on extending life or ensuring comfort?",
            "How do the patient's cultural and religious beliefs factor into this decision?",
            "What constitutes extraordinary versus ordinary care in this situation?"
        ]
    },
    'financial_services': {
        'loan_decision': [
            "Should we prioritize the applicant's current situation or historical patterns?",
            "How should we balance business risk with providing opportunity?",
            "What weight should be given to non-traditional indicators of creditworthiness?"
        ],
        'investment_advice': [
            "Is capital preservation or growth more important for this client?",
            "How should we balance automated recommendations with this client's unique circumstances?",
            "Should we consider ESG factors even if they might reduce returns?"
        ]
    },
    'content_moderation': {
        'speech_boundaries': [
            "Does this content contribute to legitimate discourse despite being offensive?",
            "Should historical/cultural context change how we evaluate this content?",
            "Is this satire/art that deserves different consideration?"
        ],
        'harm_prevention': [
            "Is there imminent risk of real-world harm from this content?",
            "Should we consider the creator's intent or focus solely on potential impact?",
            "How should we balance individual expression with community safety?"
        ]
    }
}

def get_template_question(domain, scenario_type):
    """
    Retrieve the most relevant template question
    
    Args:
        domain: The operational domain (medical, financial, etc.)
        scenario_type: Specific scenario classification
    
    Returns:
        str: Most appropriate question from templates
    """
    if domain in DOMAIN_TEMPLATES:
        if scenario_type in DOMAIN_TEMPLATES[domain]:
            questions = DOMAIN_TEMPLATES[domain][scenario_type]
            # Could add scoring logic to pick best question
            return questions[0]
    return None
```

### Layer 2: Heuristic Ethical Framing (Secondary)

When no specific template exists, generate questions using ethical frameworks.

```python
class HeuristicFramer:
    """Generate questions using ethical lenses"""
    
    ETHICAL_FRAMEWORKS = {
        'utilitarian': {
            'prompt': "Consider the greatest good for the greatest number",
            'questions': [
                "What outcome would benefit the most people?",
                "How do we weigh individual harm against collective benefit?",
                "What are the long-term consequences for all stakeholders?"
            ]
        },
        'deontological': {
            'prompt': "Focus on duties and rules",
            'questions': [
                "What rules or principles apply to this situation?",
                "Would this action be acceptable if everyone did it?",
                "Are we treating people as ends in themselves, not just means?"
            ]
        },
        'virtue_ethics': {
            'prompt': "Consider character and virtues",
            'questions': [
                "What would a virtuous person do in this situation?",
                "Does this action reflect the values we want to embody?",
                "How does this decision shape moral character?"
            ]
        },
        'care_ethics': {
            'prompt': "Focus on relationships and care",
            'questions': [
                "How does this affect the most vulnerable parties?",
                "What does caring for all stakeholders look like here?",
                "How do we maintain and honor important relationships?"
            ]
        }
    }
    
    def generate_framed_question(self, scenario_analysis):
        """
        Generate question based on relevant ethical framework
        
        Args:
            scenario_analysis: Analysis of the moral scenario
        
        Returns:
            str: Contextually framed ethical question
        """
        # Determine most relevant framework
        framework = self.select_framework(scenario_analysis)
        
        # Get base questions for that framework
        base_questions = self.ETHICAL_FRAMEWORKS[framework]['questions']
        
        # Customize based on scenario
        customized = self.customize_question(
            base_questions[0], 
            scenario_analysis
        )
        
        return customized
    
    def select_framework(self, scenario_analysis):
        """Select most appropriate ethical framework"""
        # Logic to match scenario to framework
        if 'outcomes' in scenario_analysis.keywords:
            return 'utilitarian'
        elif 'rules' in scenario_analysis.keywords:
            return 'deontological'
        elif 'vulnerable' in scenario_analysis.keywords:
            return 'care_ethics'
        else:
            return 'virtue_ethics'
    
    def customize_question(self, base_question, scenario):
        """Add scenario-specific context to question"""
        # Simple keyword replacement
        question = base_question
        if scenario.domain:
            question = f"In this {scenario.domain} context, {question.lower()}"
        return question
```

### Layer 3: Generative AI Fallback (Tertiary)

When templates and heuristics don't suffice, use guided generation.

```python
class GenerativeQuestionEngine:
    """Generate clarifying questions using LLM capabilities"""
    
    GENERATION_PROMPT = """
    Given this morally ambiguous scenario, generate 2-3 clarifying questions 
    that would help a human provide ethical guidance.
    
    Scenario: {scenario_description}
    Domain: {domain}
    Uncertainty Score: {eus_score}
    Uncertainty Factors: {uncertainty_components}
    
    Requirements for questions:
    - Focus on the core ethical dilemma
    - Be clear and specific
    - Avoid leading toward any particular answer
    - Help surface hidden assumptions
    - Respect all stakeholders involved
    
    Generate questions in order of importance:
    """
    
    def generate_questions(self, scenario_context):
        """
        Generate novel clarifying questions
        
        Args:
            scenario_context: Full context of the scenario
            
        Returns:
            list: Generated clarifying questions
        """
        prompt = self.GENERATION_PROMPT.format(
            scenario_description=scenario_context.description,
            domain=scenario_context.domain,
            eus_score=scenario_context.uncertainty_score,
            uncertainty_components=scenario_context.uncertainty_breakdown
        )
        
        # Call LLM (implementation depends on your model)
        generated = self.llm.generate(
            prompt,
            max_tokens=200,
            temperature=0.7,
            stop_sequences=["\n\n"]
        )
        
        # Parse and validate generated questions
        questions = self.parse_questions(generated)
        validated = self.validate_questions(questions, scenario_context)
        
        return validated
    
    def validate_questions(self, questions, context):
        """Ensure generated questions are appropriate"""
        validated = []
        for q in questions:
            if (self.is_clear(q) and 
                self.is_relevant(q, context) and
                self.is_unbiased(q) and
                self.is_respectful(q)):
                validated.append(q)
        return validated
```

## Question Ranking and Selection

All questions from all layers are scored and ranked.

```python
class QuestionRanker:
    """Rank and select best clarifying questions"""
    
    def rank_questions(self, questions, scenario_context):
        """
        Score and rank all available questions
        
        Args:
            questions: List of potential questions from all sources
            scenario_context: Context for relevance scoring
            
        Returns:
            list: Top-ranked questions
        """
        scored_questions = []
        
        for question in questions:
            score = self.calculate_score(question, scenario_context)
            scored_questions.append({
                'question': question,
                'score': score,
                'source': question.source  # template/heuristic/generated
            })
        
        # Sort by score
        scored_questions.sort(key=lambda x: x['score'], reverse=True)
        
        # Return top N questions
        return [q['question'] for q in scored_questions[:3]]
    
    def calculate_score(self, question, context):
        """
        Calculate question quality score
        
        Components:
        - Relevance to scenario (0-0.4)
        - Clarity and specificity (0-0.3)
        - Ethical depth (0-0.2)
        - Actionability (0-0.1)
        """
        relevance = self.score_relevance(question, context)
        clarity = self.score_clarity(question)
        depth = self.score_ethical_depth(question)
        actionable = self.score_actionability(question)
        
        return (relevance * 0.4 + 
                clarity * 0.3 + 
                depth * 0.2 + 
                actionable * 0.1)
    
    def score_relevance(self, question, context):
        """How well does question address the scenario?"""
        # Keyword overlap, semantic similarity, etc.
        keywords = extract_keywords(context.description)
        question_keywords = extract_keywords(question)
        overlap = len(keywords & question_keywords) / len(keywords)
        return min(1.0, overlap * 1.5)
    
    def score_clarity(self, question):
        """Is the question clear and specific?"""
        # Length, complexity, ambiguity checks
        optimal_length = 15  # words
        actual_length = len(question.split())
        length_score = 1 - abs(optimal_length - actual_length) / optimal_length
        
        # Check for vague terms
        vague_terms = ['thing', 'stuff', 'whatever', 'somehow']
        vagueness = sum(1 for term in vague_terms if term in question.lower())
        clarity_score = max(0, 1 - vagueness * 0.25)
        
        return (length_score + clarity_score) / 2
```

## Integration Pipeline

Complete pipeline from Sacred Pause trigger to question presentation.

```python
class ClarifyingQuestionPipeline:
    """Full clarifying question generation pipeline"""
    
    def __init__(self):
        self.template_engine = TemplateQuestionEngine()
        self.heuristic_framer = HeuristicFramer()
        self.generative_engine = GenerativeQuestionEngine()
        self.ranker = QuestionRanker()
    
    def generate_clarifying_questions(self, sacred_pause_context):
        """
        Generate optimal clarifying questions for Sacred Pause
        
        Args:
            sacred_pause_context: Complete context at pause trigger
            
        Returns:
            list: Top clarifying questions to present
        """
        all_questions = []
        
        # Layer 1: Try templates first
        template_q = self.template_engine.get_questions(
            sacred_pause_context.domain,
            sacred_pause_context.scenario_type
        )
        if template_q:
            all_questions.extend([
                {'question': q, 'source': 'template'} 
                for q in template_q
            ])
        
        # Layer 2: Add heuristic questions
        heuristic_q = self.heuristic_framer.generate_questions(
            sacred_pause_context
        )
        all_questions.extend([
            {'question': q, 'source': 'heuristic'} 
            for q in heuristic_q
        ])
        
        # Layer 3: Generate if needed
        if len(all_questions) < 3:
            generated_q = self.generative_engine.generate_questions(
                sacred_pause_context
            )
            all_questions.extend([
                {'question': q, 'source': 'generated'} 
                for q in generated_q
            ])
        
        # Rank and select best
        ranked = self.ranker.rank_questions(
            all_questions, 
            sacred_pause_context
        )
        
        return ranked[:3]  # Return top 3
```

## Response Formatting

Present questions effectively to humans.

```python
def format_clarifying_questions(questions, context):
    """
    Format questions for human presentation
    
    Args:
        questions: List of selected questions
        context: Sacred Pause context
        
    Returns:
        str: Formatted output for human review
    """
    output = f"""
    ═══════════════════════════════════════════════
    🔄 SACRED PAUSE ACTIVATED
    ═══════════════════════════════════════════════
    
    Ethical uncertainty detected (Score: {context.eus_score:.2f})
    Domain: {context.domain}
    
    The system needs your guidance on the following:
    
    """
    
    for i, question in enumerate(questions, 1):
        output += f"  {i}. {question}\n\n"
    
    output += """
    ───────────────────────────────────────────────
    Please provide your input to help resolve this
    ethical complexity. Your response will guide
    the system's decision-making.
    ═══════════════════════════════════════════════
    """
    
    return output
```

## Configuration Options

```yaml
# clarifying_questions_config.yaml
question_engine:
  layers:
    templates:
      enabled: true
      priority: 1  # Highest priority
      custom_path: "custom_templates.yaml"
    
    heuristics:
      enabled: true
      priority: 2
      frameworks:
        - utilitarian
        - deontological
        - care_ethics
    
    generative:
      enabled: true
      priority: 3  # Lowest priority
      model: "gpt-4"
      temperature: 0.7
      max_tokens: 200
  
  ranking:
    max_questions: 3
    scoring_weights:
      relevance: 0.4
      clarity: 0.3
      depth: 0.2
      actionability: 0.1
  
  presentation:
    format: "numbered"  # or "bullets", "interactive"
    include_context: true
    show_uncertainty_score: true
```

## Performance Optimization

### Caching Strategy
```python
@lru_cache(maxsize=1000)
def get_cached_questions(domain_scenario_hash):
    """Cache frequently used question combinations"""
    return generate_questions_for_scenario(domain_scenario_hash)
```

### Async Generation
```python
async def generate_questions_async(context):
    """Generate questions from all layers in parallel"""
    tasks = [
        get_template_questions_async(context),
        get_heuristic_questions_async(context),
        get_generated_questions_async(context)
    ]
    results = await asyncio.gather(*tasks)
    return flatten(results)
```

## Quality Metrics

Track these metrics to improve question generation:

1. **Human Response Rate**: How often humans provide answers
2. **Answer Completeness**: How thoroughly questions are answered
3. **Resolution Quality**: Outcome improvement after clarification
4. **Time to Response**: How quickly humans can answer
5. **Question Clarity Feedback**: Direct ratings from users

---

*The Clarifying Question Engine ensures Sacred Pause interactions are productive, generating contextually appropriate questions that help humans provide meaningful ethical guidance.*
