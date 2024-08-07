input_text = """
<a id="index"></a>
## Index
  1. [Libraries](#lib)
    1. [Open3D](#open3d)
    2. [SolidPython](#solid_python)
    3. [VPython](#vpython)
    4. [blender3d](#blender3d)
  2. [Tests](#tests)
    1. [Import Success](#import)
    2. [3d Model creation Successful](#create)
    3. [3d View Successful](#view)
  3. [Citations](#citations)
"""

def process_text(text):
    lines = text.strip().split('\n')
    result = []

    for line in lines:
        if '[' in line and '](#' in line:
            parts = line.split('[')
            name = parts[1].split(']')[0]
            link = parts[1].split('(')[1].split(')')[0]
            result.append(f'<a id="{link[1:]}"></a>\n## {name}')

    return '\n'.join(result)

output = process_text(input_text)
print(output)
