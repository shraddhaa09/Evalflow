import asyncio
from app.models.schemas import PlagiarismRequest
from app.services.plagiarism_service import score_code
from app.services.repository import repository
from app.services.model_loader import model_loader

# Force load and verify
model_loader.verify_models()
repository.load_corpus()

# Test 1: identical code to sub_0001
code_test1 = """def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1"""

req1 = PlagiarismRequest(
    code=code_test1,
    assignment_id="assignment_001",
    typing_speed_wpm=40,
    idle_ratio=0.1,
    paste_ratio=0.5,
    tab_switches=1,
    suspicion_score=0.8
)

print("\n--- TEST 1 (High Similarity) ---")
res1 = score_code(req1)
print(res1)


# Test 2: distinct code
code_test2 = """def search(a, x):
    for idx, val in enumerate(a):
        if val == x:
            return idx
    return -1
"""
req2 = PlagiarismRequest(
    code=code_test2,
    assignment_id="assignment_001",
    typing_speed_wpm=30,
    idle_ratio=0.0,
    paste_ratio=0.0,
    tab_switches=0,
    suspicion_score=0.1
)

print("\n--- TEST 2 (Low Similarity) ---")
res2 = score_code(req2)
print(res2)
