.PHONY: clean all macos linux

SC_SRC = native/macos/SelectionOverlay.swift
SC_OBJ = build/mimizu_overlay
BUILD_DIR = build
PY = python3
MAIN = main.py

all: 
	echo "does nothing"

macos: ${SC_OBJ}
	${PY} ${MAIN}

linux:
	${PY} ${MAIN}

${SC_OBJ}: ${SC_SRC}
	mkdir -p ${BUILD_DIR}
	swiftc -o ${SC_OBJ} ${SC_SRC}

clean:
	rm -rf build captures __pycache__ core/__pycache__
