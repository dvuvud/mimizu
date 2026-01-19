.PHONY: clean all

SC_SRC = native/macos/SelectionOverlay.swift
SC_OBJ = build/mimizu_overlay
BUILD_DIR = build

all: ${SC_OBJ}
	python3 main.py

${SC_OBJ}: ${SC_SRC}
	mkdir -p ${BUILD_DIR}
	swiftc -o ${SC_OBJ} ${SC_SRC}

clean:
	rm -rf build captures __pycache__ core/__pycache__
