# Compiler and linker settings
CC = gcc
CFLAGS = -Wall -g
LDFLAGS =

# Directories
SRC_DIR = src
OBJ_DIR = obj
OUT_DIR = bin
OUT_NAME = render

# Find all the source files
SRC_FILES = $(wildcard $(SRC_DIR)/*.c)
OBJ_FILES = $(SRC_FILES:$(SRC_DIR)/%.c=$(OBJ_DIR)/%.o)

# Default target to build the executable
all: $(OUT_DIR)/$(OUT_NAME)

# Rule to create the output directory if it doesn't exist
$(OUT_DIR):
	@mkdir -p $@

# Linking the object files into the final executable
$(OUT_DIR)/$(OUT_NAME): $(OBJ_FILES) | $(OUT_DIR)
	$(CC) $(OBJ_FILES) -o $@ $(LDFLAGS)

# Rule for compiling .c files to .o object files
$(OBJ_DIR)/%.o: $(SRC_DIR)/%.c | $(OBJ_DIR)
	$(CC) $(CFLAGS) -c $< -o $@

# Create the object directory if it doesn't exist
$(OBJ_DIR):
	@mkdir -p $@

# Clean up compiled files
clean:
	rm -rf $(OBJ_DIR) $(OUT_DIR)