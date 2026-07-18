---
name: Aether Seismic Design System
colors:
  surface: '#0d150e'
  surface-dim: '#0d150e'
  surface-bright: '#323c33'
  surface-container-lowest: '#081009'
  surface-container-low: '#151e16'
  surface-container: '#19221a'
  surface-container-high: '#232c24'
  surface-container-highest: '#2e372e'
  on-surface: '#dbe5d9'
  on-surface-variant: '#bacbb9'
  inverse-surface: '#dbe5d9'
  inverse-on-surface: '#29332a'
  outline: '#859585'
  outline-variant: '#3b4a3d'
  surface-tint: '#00e475'
  primary: '#75ff9e'
  on-primary: '#003918'
  primary-container: '#00e676'
  on-primary-container: '#00612e'
  inverse-primary: '#006d35'
  secondary: '#ffb4aa'
  on-secondary: '#690003'
  secondary-container: '#c5020b'
  on-secondary-container: '#ffd2cc'
  tertiary: '#ffdec4'
  on-tertiary: '#4b2800'
  tertiary-container: '#ffba79'
  on-tertiary-container: '#794810'
  error: '#ffb4ab'
  on-error: '#690005'
  error-container: '#93000a'
  on-error-container: '#ffdad6'
  primary-fixed: '#62ff96'
  primary-fixed-dim: '#00e475'
  on-primary-fixed: '#00210b'
  on-primary-fixed-variant: '#005226'
  secondary-fixed: '#ffdad5'
  secondary-fixed-dim: '#ffb4aa'
  on-secondary-fixed: '#410001'
  on-secondary-fixed-variant: '#930005'
  tertiary-fixed: '#ffdcbf'
  tertiary-fixed-dim: '#fdb878'
  on-tertiary-fixed: '#2d1600'
  on-tertiary-fixed-variant: '#6a3c03'
  background: '#0d150e'
  on-background: '#dbe5d9'
  surface-variant: '#2e372e'
typography:
  display-xl:
    fontFamily: Geist
    fontSize: 48px
    fontWeight: '700'
    lineHeight: '1.1'
    letterSpacing: -0.04em
  headline-lg:
    fontFamily: Geist
    fontSize: 24px
    fontWeight: '600'
    lineHeight: '1.2'
    letterSpacing: -0.02em
  headline-md:
    fontFamily: Geist
    fontSize: 20px
    fontWeight: '500'
    lineHeight: '1.3'
  body-md:
    fontFamily: Inter
    fontSize: 14px
    fontWeight: '400'
    lineHeight: '1.6'
  code-sm:
    fontFamily: JetBrains Mono
    fontSize: 12px
    fontWeight: '400'
    lineHeight: '1.4'
    letterSpacing: 0.05em
  label-caps:
    fontFamily: JetBrains Mono
    fontSize: 11px
    fontWeight: '700'
    lineHeight: '1.2'
    letterSpacing: 0.1em
rounded:
  sm: 0.125rem
  DEFAULT: 0.25rem
  md: 0.375rem
  lg: 0.5rem
  xl: 0.75rem
  full: 9999px
spacing:
  unit: 4px
  container-padding: 24px
  component-gap: 16px
  grid-margin: 32px
  panel-width-side: 320px
---

## Brand & Style
The design system establishes a high-fidelity, mission-critical environment for advanced seismic interpretation. It blends the structural rigor of SpaceX Mission Control with the spatial elegance of Apple Vision Pro. The aesthetic is "Advanced Volumetric," characterized by deep spatial depth, scientific precision, and a high-tech utility that commands authority in the oil and gas sector.

The visual narrative is built on:
- **Futuristic Glassmorphism:** Surfaces utilize frosted translucency to maintain a sense of layered complexity without sacrificing legibility.
- **Scientific Minimalism:** Every pixel serves a functional purpose; decorative elements are replaced with data-driven accents like coordinate grids and technical metadata.
- **Kinetic Feedback:** Glowing interactive states and precise micro-animations evoke the feeling of a living, breathing AI engine.

## Colors
The palette is rooted in a "Deep Space" background strategy using a dark navy base with subtle radial gradients to create depth. 

- **Ground Truth (#00E676):** Used for verified data, successful inferences, and primary action confirmation.
- **Prediction (#FF3B30):** Used for AI-generated hypotheses, anomalies, and critical system errors.
- **Atmospheric Accents:** Cyan is used for instrumentation and active states to differentiate UI controls from data markers.
- **Glass Surfaces:** Containers use a semi-transparent dark navy fill with a fine 1px inner stroke to simulate physical glass depth.

## Typography
The typography system prioritizes high-density information display and technical clarity.

- **Geist** is used for headlines to provide a sharp, developer-centric aesthetic that feels engineered.
- **Inter** provides neutral, high-legibility body text for long-form reports and data descriptions.
- **JetBrains Mono** is reserved for metadata, coordinate values, and system readouts, reinforcing the "instrumentation" feel of the platform.
- **Strict Hierarchy:** Utilize `label-caps` for all section headers and slider titles to maintain a structured, cockpit-like organization.

## Layout & Spacing
The layout follows a **Fixed-Side-Fluid-Center** model to maximize the 3D viewport area while keeping analysis tools pinned.

- **Sidebar Panels:** Fixed at 320px to accommodate complex controls and vertical data lists.
- **The Grid:** A 12-column layout for dashboard views, but primary interpretation screens use a "Workbench" layout where tools float over the main volumetric viewer.
- **Density:** High-density spacing (4px/8px increments) is required to pack mission-critical information into a single view without scrolling.
- **Safe Zones:** 32px margins around the screen edge prevent UI elements from feeling cramped against the hardware bezel.

## Elevation & Depth
Elevation is expressed through **transparency and blur** rather than traditional drop shadows.

- **Level 1 (Base):** Dark navy background with a subtle noise texture to prevent banding in gradients.
- **Level 2 (Glass Containers):** `background-blur: 20px`, 65% opacity, and a 1px solid border (`#ffffff10`).
- **Level 3 (Interactive/Active):** Surfaces receive a "Glow" effect using an outer neon stroke (Primary Green or Cyan) with a 10px Gaussian blur.
- **Z-Axis layering:** Use CSS `z-index` to ensure tooltips and modal overlays clearly sit "above" the 3D volumetric space.

## Shapes
The design system utilizes a "Technical Soft" shape language. 

- **Primary Corners:** 4px (0.25rem) for a precision-machined look.
- **Large Panels:** 8px (0.5rem) to provide a subtle structural softness to the large glass containers.
- **Interactive Elements:** Buttons and toggles use the 4px radius to feel like physical hardware buttons.
- **Circular Elements:** Reserved strictly for status indicators, avatars, and specific playback controls (Play/Pause).

## Components
- **Glassmorphic Cards:** Feature a top-down light source reflected in the 1px border. The header area should be slightly more opaque than the body.
- **Data Sliders:** Custom thin-track sliders with glowing "thumb" indicators. The value readout should be in `JetBrains Mono`.
- **Status Badges:** Pill-shaped with a pulse animation for "Live" states. Ground Truth badges use a solid green fill with black text.
- **3D Viewport Controls:** Floating, semi-transparent icon clusters located in the corners of the viewer for "Reset View," "Toggle Grid," and "Snapshot."
- **Inference Buttons:** Large-format buttons with a gradient fill. The "Run Prediction" button should use a subtle inner glow to signify it as the primary system trigger.
- **File Lists:** Rows should have a hover state that lightens the background blur and reveals a secondary "Download" or "Inspect" action.