"""
Customer Service Chatbot
A simple rule-based chatbot for handling basic customer service queries
"""

import re
import string

# ========================
# CHATBOT KNOWLEDGE BASE
# ========================

# Define bot responses for different intents
RESPONSES = {
    'greeting': [
        "Hello! Welcome to our customer service. How can I help you today?",
        "Hi there! I'm here to assist you. What can I do for you?",
        "Hey! Thanks for reaching out. How may I help you?"
    ],
    
    'business_hours': [
        "Our business hours are Monday to Friday, 9:00 AM to 6:00 PM, and Saturday 10:00 AM to 4:00 PM. We're closed on Sundays.",
        "We're open Mon-Fri: 9 AM - 6 PM, Saturday: 10 AM - 4 PM. Closed on Sundays."
    ],
    
    'contact': [
        "You can reach us at:\n📞 Phone: 1-800-123-4567\n📧 Email: support@company.com\n💬 Live Chat: Available on our website",
        "Contact us via phone at 1-800-123-4567 or email at support@company.com. We also have live chat on our website!"
    ],
    
    'products': [
        "We offer a wide range of products including electronics, clothing, home goods, and more. Visit our website to browse our full catalog!",
        "Our product categories include: Electronics, Fashion, Home & Living, Sports & Outdoors, and Beauty. What are you interested in?"
    ],
    
    'order_status': [
        "To check your order status, please provide your order number. You can also track it on our website under 'My Orders' section.",
        "I can help you track your order! Please log into your account or provide your order number and email address."
    ],
    
    'return_policy': [
        "Our return policy: You can return items within 30 days of purchase for a full refund. Items must be unused and in original packaging.",
        "We accept returns within 30 days. Items should be in original condition with tags attached. Refunds are processed within 5-7 business days."
    ],
    
    'refund': [
        "Refunds are processed within 5-7 business days after we receive your returned item. The amount will be credited to your original payment method.",
        "Once we receive your return, refunds typically take 5-7 business days to process and appear in your account."
    ],
    
    'shipping': [
        "We offer free standard shipping on orders over $50. Express shipping is available for $9.99. Delivery takes 3-7 business days.",
        "Shipping options: Standard (3-7 days, free over $50), Express (2-3 days, $9.99), Overnight ($24.99)"
    ],
    
    'payment': [
        "We accept all major credit cards (Visa, MasterCard, Amex), PayPal, and Apple Pay.",
        "Payment methods: Credit/Debit cards, PayPal, Apple Pay, Google Pay, and Affirm for financing."
    ],
    
    'help': [
        "I can assist you with:\n- Business hours\n- Contact information\n- Product information\n- Order status\n- Returns and refunds\n- Shipping details\n- Payment options\n\nWhat would you like to know?"
    ],
    
    'thanks': [
        "You're welcome! Is there anything else I can help you with?",
        "Happy to help! Let me know if you need anything else.",
        "My pleasure! Feel free to ask if you have more questions."
    ],
    
    'goodbye': [
        "Thank you for contacting us! Have a great day!",
        "Goodbye! Feel free to reach out anytime you need assistance.",
        "Take care! We're here whenever you need us."
    ]
}

# Keywords for intent detection
INTENT_KEYWORDS = {
    'greeting': ['hello', 'hi', 'hey', 'greetings', 'good morning', 'good afternoon', 'good evening'],
    'business_hours': ['hours', 'open', 'close', 'timing', 'schedule', 'when open', 'availability'],
    'contact': ['contact', 'phone', 'email', 'reach', 'call', 'message', 'support'],
    'products': ['product', 'products', 'item', 'items', 'catalog', 'what do you sell', 'what sell'],
    'order_status': ['order', 'track', 'tracking', 'status', 'where is my order', 'shipment'],
    'return_policy': ['return', 'returns', 'return policy', 'send back'],
    'refund': ['refund', 'money back', 'reimburse', 'reimbursement'],
    'shipping': ['shipping', 'delivery', 'ship', 'deliver', 'shipping cost', 'how long'],
    'payment': ['payment', 'pay', 'credit card', 'paypal', 'how to pay', 'payment method'],
    'help': ['help', 'assist', 'support', 'what can you do', 'options'],
    'thanks': ['thank', 'thanks', 'appreciate', 'grateful'],
    'goodbye': ['bye', 'goodbye', 'exit', 'quit', 'see you', 'later']
}


# ========================
# NLP PROCESSING FUNCTIONS
# ========================

def preprocess_text(text):
    """
    Clean and normalize user input
    - Convert to lowercase
    - Remove punctuation
    - Remove extra whitespace
    """
    # Convert to lowercase
    text = text.lower()
    
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Remove extra whitespace
    text = ' '.join(text.split())
    
    return text


def detect_intent(user_input):
    """
    Detect user intent based on keywords in the input
    Returns the matched intent or None
    """
    # Preprocess the input
    processed_input = preprocess_text(user_input)
    
    # Check each intent's keywords
    for intent, keywords in INTENT_KEYWORDS.items():
        for keyword in keywords:
            if keyword in processed_input:
                return intent
    
    # No intent matched
    return None


def get_response(intent):
    """
    Get appropriate response based on detected intent
    Returns the first response for the intent
    """
    if intent and intent in RESPONSES:
        # Return the first response for this intent
        return RESPONSES[intent][0]
    else:
        # Fallback response for unknown queries
        return ("I'm not sure I understood that. I can help you with business hours, "
                "contact info, products, orders, returns, shipping, and payments. "
                "What would you like to know?")


# ========================
# MAIN CHATBOT FUNCTION
# ========================

def run_chatbot():
    """
    Main function to run the customer service chatbot
    """
    # Welcome message
    print("=" * 60)
    print("         CUSTOMER SERVICE CHATBOT")
    print("=" * 60)
    print("Welcome! I'm here to help with your questions.")
    print("Type 'exit' or 'quit' to end the conversation.")
    print("=" * 60)
    print()
    
    # Main conversation loop
    while True:
        # Get user input
        user_input = input("You: ").strip()
        
        # Check if user wants to exit
        if user_input.lower() in ['exit', 'quit', 'bye', 'goodbye']:
            print("\nBot:", get_response('goodbye'))
            print("\n" + "=" * 60)
            print("Thank you for using our customer service!")
            print("=" * 60)
            break
        
        # Skip empty input
        if not user_input:
            continue
        
        # Detect intent and generate response
        intent = detect_intent(user_input)
        response = get_response(intent)
        
        # Display bot response
        print(f"\nBot: {response}\n")


# ========================
# PROGRAM ENTRY POINT
# ========================

if __name__ == "__main__":
    run_chatbot()
