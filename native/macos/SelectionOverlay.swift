#!/usr/bin/env swift
import Cocoa
import Foundation

class SelectionView: NSView {
    var startPoint: NSPoint?
    var endPoint: NSPoint?
    private let borderWidth: CGFloat = 2.0
    
    override var acceptsFirstResponder: Bool { return true }
    
    override func keyDown(with event: NSEvent) {
        if event.keyCode == 53 { // ESC
            print("PNG_DATA:null")
            NSApp.terminate(nil)
        }
    }
    
    override func mouseDown(with event: NSEvent) {
        startPoint = convert(event.locationInWindow, from: nil)
        endPoint = startPoint
        needsDisplay = true
    }
    
    override func mouseDragged(with event: NSEvent) {
        endPoint = convert(event.locationInWindow, from: nil)
        needsDisplay = true
    }
    
    override func mouseUp(with event: NSEvent) {
        guard let start = startPoint, let end = endPoint else {
            print("PNG_DATA:null")
            NSApp.terminate(nil)
            return
        }
        
        let captureRect = NSRect( // Exclude border from capture
            x: min(start.x, end.x) + borderWidth,
            y: min(start.y, end.y) + borderWidth,
            width: abs(end.x - start.x) - borderWidth * 2,
            height: abs(end.y - start.y) - borderWidth * 2
        )
        
        guard captureRect.width > 0 && captureRect.height > 0 else {
            print("PNG_DATA:null")
            NSApp.terminate(nil)
            return
        }
        
        guard let screen = NSScreen.main else {
            print("PNG_DATA:null")
            NSApp.terminate(nil)
            return
        }
        
        let screenFrame = screen.frame
        let screenHeight = screenFrame.height
        
        let cgRect = CGRect(
            x: captureRect.origin.x,
            y: screenHeight - captureRect.maxY,
            width: captureRect.width,
            height: captureRect.height
        )
        
        guard let image = CGWindowListCreateImage(cgRect, .optionOnScreenOnly, kCGNullWindowID, .bestResolution) else {
            print("PNG_DATA:null")
            NSApp.terminate(nil)
            return
        }
        
        let bitmap = NSBitmapImageRep(cgImage: image)
        guard let pngData = bitmap.representation(using: .png, properties: [:]) else {
            print("PNG_DATA:null")
            NSApp.terminate(nil)
            return
        }
        
        let base64String = pngData.base64EncodedString()
        print("PNG_DATA:\(base64String)")
        
        NSApp.terminate(nil)
    }
    
    override func draw(_ dirtyRect: NSRect) {
        NSColor.clear.set()
        bounds.fill()
        
        guard let start = startPoint, let end = endPoint else { return }
        
        let drawRect = NSRect(
            x: min(start.x, end.x),
            y: min(start.y, end.y),
            width: abs(end.x - start.x),
            height: abs(end.y - start.y)
        )
        
        let path = NSBezierPath(rect: drawRect)
        path.lineWidth = borderWidth
        let dashPattern: [CGFloat] = [8.0, 4.0]
        path.setLineDash(dashPattern, count: 2, phase: 0)
        NSColor.white.setStroke()
        path.stroke()
    }
}

setbuf(__stdoutp, nil)

guard let screen = NSScreen.main else {
    exit(1)
}

let screenFrame = screen.frame

let window = NSWindow(
    contentRect: screenFrame,
    styleMask: .borderless,
    backing: .buffered,
    defer: false
)

window.level = .screenSaver
window.backgroundColor = .clear
window.isOpaque = false
window.collectionBehavior = [.canJoinAllSpaces, .fullScreenAuxiliary]
window.ignoresMouseEvents = false

window.setFrameOrigin(NSPoint(x: 0, y: 0))

let contentView = SelectionView(frame: screenFrame)
window.contentView = contentView

window.makeKeyAndOrderFront(nil)
window.makeFirstResponder(contentView)
NSApp.activate(ignoringOtherApps: true)

NSApp.setActivationPolicy(.accessory)
NSApp.run()
