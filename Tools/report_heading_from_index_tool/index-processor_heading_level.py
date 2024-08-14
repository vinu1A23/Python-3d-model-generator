def process_text(text):
    lines = text.strip().split('\n')
    result = []
    for line in lines:
        if '[' in line and '](#' in line:
            # Count leading spaces to determine heading level
            leading_spaces = len(line) - len(line.lstrip())
            heading_level = leading_spaces // 4 + 2  # 4 spaces represent a step down

            parts = line.split('[')
            name = parts[1].split(']')[0]
            link = parts[1].split('(')[1].split(')')[0]

            # Create heading with appropriate number of '#' symbols
            heading = '#' * heading_level

            result.append(f'<a id="{link[1:]}"></a>\n\n\n\n\n{heading} {name}\n\n\n\n')
    return '\n'.join(result)

# Test the function
input_text = """
1. [Environment Setup](#env)
        1. [Endeavour OS](#endeavour)
        2. [Python 3.12](#py3.12)
        3. [Kate](#kate)
        4. [pip 24.2](#pip2.42)
        5. [SolidPython 2](#solid2)
2. [Experiments Methodology](#methodology)
    1. [Libraries](#lib)
        1. [Open3D](#open3d)
        2. [SolidPython](#solid_python)
        3. [VPython](#vpython)
        4. [blender3d](#blender3d)
    2. [Tests](#tests)
        1. [Import Success](#import)
        2. [3d Model creation Successful](#create)
        3. [3d View Successful](#view)
3. [Results](#results)
4. [Citations](#citations)
"""

output = process_text(input_text)
print(output)
