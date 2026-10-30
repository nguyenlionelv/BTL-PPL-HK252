import re

path = r'd:\Users\BuiTrongNguyen\[HK252] PPL\BTL-PPL-HK252\tests\test_checker.py'
with open(path, encoding='utf-8') as f:
    content = f.read()

tests = re.findall(r'def test_checker_(\d+)\(', content)
nums = sorted([int(n) for n in tests])
print(f'Total tests: {len(nums)}')
print(f'First: {nums[0]}, Last: {nums[-1]}')

gaps = []
for i in range(1, len(nums)):
    if nums[i] - nums[i-1] > 1:
        gaps.append((nums[i-1], nums[i]))

if gaps:
    print(f'Gaps: {gaps}')
else:
    print('No gaps - continuous 1 to', nums[-1])

import os
os.remove(r'd:\Users\BuiTrongNguyen\[HK252] PPL\BTL-PPL-HK252\tests\_append_tests.py')
print('Helper file removed.')
