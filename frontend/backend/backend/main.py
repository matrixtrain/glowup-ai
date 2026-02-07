from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import random
import io

app = FastAPI(title="GlowUp AI API", description="AI-powered personalized glow up tips API", version="1.0")

# Allow Frontend to access API from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_methods=["*"],
    allow_headers=["*"],
)

# Skin types & face shapes
SKIN_TYPES = ["Oily", "Dry", "Combination", "Normal"]
FACE_SHAPES = ["Oval", "Round", "Square", "Heart"]

# Glow tips for each skin type
GLOW_TIPS = {
    "Oily": [
        "Use gentle cleanser twice daily",
        "Avoid heavy oils",
        "Clay mask weekly"
    ],
    "Dry": [
        "Moisturize morning and night",
        "Avoid hot water",
        "Use hyaluronic serum"
    ],
    "Combination": [
        "Balance skincare for T-zone",
        "Use lightweight moisturizer",
        "Exfoliate twice weekly"
    ],
    "Normal": [
        "Maintain your routine",
        "Use sunscreen daily",
        "Stay hydrated"
    ]
}

# 7-Day Glow Up Plan
GLOW_PLAN = {
    "Oily": [
        "Day 1: Gentle cleanser + drink 2L water",
        "Day 2: Ice your face + sleep 8 hours",
        "Day 3: Clay mask + avoid junk food",
        "Day 4: Sunscreen + light workout",
        "Day 5: Gentle exfoliation",
        "Day 6: Clean pillowcase + hydration",
        "Day 7: Confidence – smile & posture"
    ],
    "Dry": [
        "Day 1: Deep moisturizer + water",
        "Day 2: Avoid hot water",
        "Day 3: Hyaluronic serum",
        "Day 4: Eat healthy fats (nuts, olive oil)",
        "Day 5: Gentle exfoliation",
        "Day 6: Early sleep",
        "Day 7: Skin massage + confidence"
    ],
    "Combination": [
        "Day 1: Gentle cleanser + hydration",
        "Day 2: Light moisturizer + exercise",
        "Day 3: Exfoliation + diet",
        "Day 4: Sunscreen + meditation",
        "Day 5: Mask + hydration",
        "Day 6: Early sleep + clean pillowcase",
        "Day 7: Confidence + smile"
    ],
    "Normal": [
        "Day 1: Maintain routine + sunscreen",
        "Day 2: Drink water + light exercise",
        "Day 3: Gentle exfoliation",
        "Day 4: Hydration + sleep",
        "Day 5: Healthy diet",
        "Day 6: Mask + skincare",
        "Day 7: Confidence day – posture & smile"
    ]
}

@app.post("/analyze")
async def analyze_face(photo: UploadFile = File(...)):
    """
    Analyze face and return skin type, face shape, glow tips, and a 7-day plan.
    Currently uses random selection for demonstration.
    """

    # Optional: check file type
    if not photo.content_type.startswith("image/"):
        return JSONResponse(status_code=400, content={"error": "Invalid file type. Please upload an image."})

    # Read the image (optional, not processing real AI yet)
    img_bytes = await photo.read()
    image_size = len(img_bytes) / 1024  # KB
    print(f"Received image: {photo.filename} ({image_size:.2f} KB)")

    # Random selection for demo
    skin = random.choice(SKIN_TYPES)
    shape = random.choice(FACE_SHAPES)

    return {
        "skin_type": skin,
        "face_shape": shape,
        "tips": GLOW_TIPS[skin],
        "plan": GLOW_PLAN[skin]
    }

@app.get("/")
async def root():
    return {"message": "GlowUp AI API is live! POST your photo to /analyze to get personalized glow up tips."}
