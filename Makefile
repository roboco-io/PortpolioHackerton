# MARP Slides Makefile
# Usage:
#   make all          - Build all slides (HTML + PPTX)
#   make html         - Build all HTML slides
#   make pptx         - Build all PPTX slides
#   make slides/01-Intro.html  - Build specific HTML
#   make slides/01-Intro.pptx  - Build specific PPTX
#   make clean        - Remove all generated files
#   make watch        - Watch for changes and rebuild

# Directories
SLIDES_DIR := slides
OUTPUT_DIR := slides/output

# Find all markdown files in slides directory
MD_FILES := $(wildcard $(SLIDES_DIR)/*.md)

# Generate output file paths
HTML_FILES := $(patsubst $(SLIDES_DIR)/%.md,$(OUTPUT_DIR)/%.html,$(MD_FILES))
PPTX_FILES := $(patsubst $(SLIDES_DIR)/%.md,$(OUTPUT_DIR)/%.pptx,$(MD_FILES))

# MARP CLI command
MARP := npx @marp-team/marp-cli

# MARP options
MARP_OPTS := --allow-local-files

# Default target
.PHONY: all
all: html pptx

# Build all HTML files
.PHONY: html
html: $(HTML_FILES)

# Build all PPTX files
.PHONY: pptx
pptx: $(PPTX_FILES)

# Create output directory
$(OUTPUT_DIR):
	@mkdir -p $(OUTPUT_DIR)

# Pattern rule for HTML
$(OUTPUT_DIR)/%.html: $(SLIDES_DIR)/%.md | $(OUTPUT_DIR)
	@echo "Building HTML: $<"
	$(MARP) $(MARP_OPTS) $< -o $@

# Pattern rule for PPTX
$(OUTPUT_DIR)/%.pptx: $(SLIDES_DIR)/%.md | $(OUTPUT_DIR)
	@echo "Building PPTX: $<"
	$(MARP) $(MARP_OPTS) $< -o $@

# Build specific slide (both formats)
# Usage: make slide NAME=01-Intro
.PHONY: slide
slide:
ifndef NAME
	$(error NAME is required. Usage: make slide NAME=01-Intro)
endif
	@$(MAKE) $(OUTPUT_DIR)/$(NAME).html
	@$(MAKE) $(OUTPUT_DIR)/$(NAME).pptx

# Watch mode for development
.PHONY: watch
watch:
	$(MARP) $(MARP_OPTS) -w $(SLIDES_DIR)/*.md -o $(OUTPUT_DIR)

# Preview specific slide in browser
# Usage: make preview NAME=01-Intro
.PHONY: preview
preview:
ifndef NAME
	$(error NAME is required. Usage: make preview NAME=01-Intro)
endif
	$(MARP) $(MARP_OPTS) -p $(SLIDES_DIR)/$(NAME).md

# Clean generated files
.PHONY: clean
clean:
	@echo "Cleaning generated files..."
	@rm -rf $(OUTPUT_DIR)
	@echo "Done."

# List all available slides
.PHONY: list
list:
	@echo "Available slides:"
	@for f in $(MD_FILES); do echo "  - $$(basename $$f .md)"; done

# Help
.PHONY: help
help:
	@echo "MARP Slides Makefile"
	@echo ""
	@echo "Usage:"
	@echo "  make all                    Build all slides (HTML + PPTX)"
	@echo "  make html                   Build all HTML slides"
	@echo "  make pptx                   Build all PPTX slides"
	@echo "  make slide NAME=<name>      Build specific slide (both formats)"
	@echo "  make preview NAME=<name>    Preview specific slide in browser"
	@echo "  make watch                  Watch for changes and rebuild"
	@echo "  make clean                  Remove all generated files"
	@echo "  make list                   List all available slides"
	@echo ""
	@echo "Examples:"
	@echo "  make slide NAME=01-Intro"
	@echo "  make slides/output/01-Intro.html"
	@echo "  make slides/output/01-Intro.pptx"
