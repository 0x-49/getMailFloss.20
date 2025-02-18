import os
import re
from pathlib import Path
from typing import List, Dict

class AstroFileCombiner:
    def __init__(self, src_dir: str, output_file: str = "combined_astro_output.txt"):
        self.src_dir = Path(src_dir)
        self.output_file = output_file
        self.component_map: Dict[str, str] = {}
        
    def find_astro_files(self) -> List[Path]:
        """Find all .astro files in the project."""
        return list(self.src_dir.rglob("*.astro"))
    
    def read_file_content(self, file_path: Path) -> str:
        """Read and return the content of a file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                return f.read()
        except Exception as e:
            print(f"Error reading {file_path}: {e}")
            return ""

    def extract_component_name(self, file_path: Path) -> str:
        """Extract component name from file path."""
        return file_path.stem

    def process_file(self, file_path: Path) -> None:
        """Process individual Astro file and store its content."""
        content = self.read_file_content(file_path)
        component_name = self.extract_component_name(file_path)
        relative_path = file_path.relative_to(self.src_dir)
        
        # Store the component with its metadata
        self.component_map[str(relative_path)] = {
            'name': component_name,
            'content': content,
            'path': str(relative_path)
        }

    def combine_files(self) -> None:
        """Combine all Astro files into a single output file."""
        astro_files = self.find_astro_files()
        
        for file_path in astro_files:
            self.process_file(file_path)

        # Write combined output
        with open(self.output_file, 'w', encoding='utf-8') as f:
            f.write("# Combined Astro Components\n\n")
            
            for path, data in sorted(self.component_map.items()):
                f.write(f"## Component: {data['name']}\n")
                f.write(f"### Path: {data['path']}\n")
                f.write("```astro\n")
                f.write(data['content'])
                f.write("\n```\n\n")
                f.write("-".center(80, "-") + "\n\n")

    def analyze_components(self) -> Dict:
        """Analyze components for dependencies and structure."""
        analysis = {
            'total_components': len(self.component_map),
            'component_list': list(self.component_map.keys()),
            'structure': {}
        }
        
        # Group components by directory
        for path in self.component_map.keys():
            parts = Path(path).parts
            current_dict = analysis['structure']
            for part in parts[:-1]:
                if part not in current_dict:
                    current_dict[part] = {}
                current_dict = current_dict[part]
            current_dict[parts[-1]] = None
            
        return analysis

def main():
    # Update this path to match your project's src directory
    src_dir = r"c:\personal\LandingPage Affialte SEO\final_2\MailFloss\AstroMail\src"
    combiner = AstroFileCombiner(src_dir)
    
    print("Starting Astro files combination process...")
    combiner.combine_files()
    
    analysis = combiner.analyze_components()
    print(f"\nProcessed {analysis['total_components']} components")
    print("\nComponent structure:")
    for component in analysis['component_list']:
        print(f"- {component}")
    
    print(f"\nOutput written to: {combiner.output_file}")

if __name__ == "__main__":
    main()
