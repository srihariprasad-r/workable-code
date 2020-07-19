"""
Given a string, print all possible substrings
"""

def generateAllSubstring(s):
  for i in range(len(s)):
    for j in range(i+1, len(s)+1):
      print(s[i:j])

s = "eceba"
generateAllSubstring(s)     