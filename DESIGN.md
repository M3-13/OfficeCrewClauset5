# Design — Project Identity

> This document is project-long-lived. Tokens are not changed without
> the Architect's approval. Developers MUST use these tokens
> instead of improvising their own colors/spacings.

## Style Direction

Samtig-dunkles Red-Carpet-Ambiente: tiefer Anthrazit-Hintergrund, warme Gold-Akzente und Burgunderrot als dramatischer Sekundärton. Elegante Serifen-Überschriften treffen auf kühle Sachlichkeit im Fließtext – wie der Backstage-Bereich einer Gala, der Funktionalität und Glamour vereint. Spotlight-Hover auf jeder Karte inszeniert jedes Kleidungsstück wie unter einem Scheinwerfer.

## Colors

- `--color-bg`: **#0B0B0C**
- `--color-surface`: **#161618**
- `--color-surface_raised`: **#1E1E21**
- `--color-fg`: **#F2EEE7**
- `--color-fg_muted`: **#9D9790**
- `--color-accent`: **#D4AF37**
- `--color-accent_hover`: **#E5C85C**
- `--color-accent_dim`: **#A68B1F**
- `--color-burgundy`: **#8B1E2F**
- `--color-burgundy_light`: **#B52D43**
- `--color-burgundy_surface`: **#1A0D10**
- `--color-border`: **#2A2A2E**
- `--color-border_light`: **#3D3C40**
- `--color-success`: **#4CAF88**
- `--color-error`: **#E05555**
- `--color-spotlight`: **radial-gradient(ellipse at center, rgba(212,175,55,0.18) 0%, transparent 70%)**

## Typography

- `font_family`: 'Inter', 'Helvetica Neue', Arial, sans-serif
- `heading_font_family`: 'Playfair Display', 'Cormorant Garamond', Georgia, 'Times New Roman', serif
- `heading_weight`: 700
- `body_weight`: 400
- `body_size`: 16px
- `size_scale`: xs: 0.75rem; sm: 0.875rem; base: 1rem; lg: 1.125rem; xl: 1.25rem; 2xl: 1.5rem; 3xl: 2rem; 4xl: 2.75rem; hero: 3.5rem

## Spacing Scale

- `--space-0`: 4px
- `--space-1`: 8px
- `--space-2`: 12px
- `--space-3`: 16px
- `--space-4`: 24px
- `--space-5`: 32px
- `--space-6`: 48px
- `--space-7`: 64px

## Border-Radii

- `--radius-sm`: 4px
- `--radius-md`: 8px
- `--radius-lg`: 16px
- `--radius-xl`: 24px
- `--radius-pill`: 999px

## Components

### Button (Primary – Gold)

padding 12px 24px, radius md, bg=accent(#D4AF37), color=#0B0B0C, font-weight 600, text-transform uppercase, letter-spacing 0.05em, min-height 44px, border none. Hover: bg=accent_hover(#E5C85C), box-shadow 0 0 20px rgba(212,175,55,0.35), scale 1.03, transition all 200ms ease-out. Active: bg=accent_dim(#A68B1F), scale 0.98. Disabled: opacity 0.4, pointer-events none, filter grayscale(30%). Focus-visible: outline 2px solid #E5C85C, outline-offset 2px.

### Button (Secondary – Outline)

padding 10px 22px, radius md, bg=transparent, color=#F2EEE7, border 1.5px solid #3D3C40, min-height 44px. Hover: border-color=accent(#D4AF37), color=accent(#D4AF37), bg=rgba(212,175,55,0.06). Active: bg=rgba(212,175,55,0.12). Disabled: opacity 0.35, pointer-events none.

### Button (Danger – Burgundy)

padding 12px 24px, radius md, bg=burgundy(#8B1E2F), color=#F2EEE7, min-height 44px. Hover: bg=burgundy_light(#B52D43), box-shadow 0 0 16px rgba(139,30,47,0.3). Active: bg=#6E1523. Disabled: opacity 0.4, pointer-events none.

### Card (Kleidungsstück)

bg=surface(#161618), border 1px solid border(#2A2A2E), radius lg(16px), overflow hidden, padding 0 (image fills top), content padding 16px. Hover: border-color=rgba(212,175,55,0.45), box-shadow 0 8px 32px rgba(0,0,0,0.5) + spotlight radial gradient overlay, transform translateY(-4px), transition all 300ms cubic-bezier(0.25,0.46,0.45,0.94). Image area: aspect-ratio 3/4, object-fit cover, bg=#1A1A1D. Caption: font_family heading, size sm, color fg_muted, text-transform uppercase, letter-spacing 0.08em.

### Input Field

bg=#0B0B0C, border 1.5px solid border(#2A2A2E), radius md(8px), padding 12px 16px, color=fg(#F2EEE7), font-size base, min-height 48px. Placeholder: color=#5C5852. Focus: border-color=accent(#D4AF37), box-shadow 0 0 0 3px rgba(212,175,55,0.12), outline none. Error: border-color=error(#E05555), box-shadow 0 0 0 3px rgba(224,85,85,0.10). Disabled: opacity 0.4, bg=#111113.

### Badge / Category Tag

display inline-flex, padding 4px 12px, radius pill(999px), bg=burgundy_surface(#1A0D10), color=burgundy_light(#B52D43), font-size xs, font-weight 600, letter-spacing 0.04em, text-transform uppercase, border 1px solid rgba(139,30,47,0.3). Gold-variant: bg=rgba(212,175,55,0.08), color=accent(#D4AF37), border 1px solid rgba(212,175,55,0.25).

### Modal / Overlay

Backdrop: bg=rgba(0,0,0,0.75), backdrop-filter blur(8px). Panel: bg=surface_raised(#1E1E21), border 1px solid border_light(#3D3C40), radius xl(24px), padding 32px, max-width 560px, width 90vw, box-shadow 0 24px 80px rgba(0,0,0,0.6). Close button: top 16px, right 16px, size 36px, radius pill, bg=transparent, color=fg_muted, hover: bg=rgba(255,255,255,0.06), color=fg. Title: font_family heading, size 3xl, color=accent, mb 24px.

### NavBar (Top)

bg=rgba(11,11,12,0.85), backdrop-filter blur(16px), border-bottom 1px solid border(#2A2A2E), height 64px, padding 0 24px, display flex, align-items center, position sticky top 0, z-index 50. Logo/Title: font_family heading, size xl, color=accent(#D4AF37), letter-spacing 0.04em. Nav links: color=fg_muted, font-size sm, text-transform uppercase, letter-spacing 0.06em, padding 8px 16px, radius sm. Hover: color=fg, bg=rgba(255,255,255,0.04). Active: color=accent.

### Outfit-Creator Layout (zweispaltig)

Container: display grid, grid-template-columns 1fr 400px, gap 24px, min-height calc(100vh - 64px). Linke Spalte (Garderobe): bg=surface(#161618), border 1px solid border, radius lg, padding 24px, overflow-y auto. Filter-Leiste: flex, gap 12px, mb 20px. Grid der Kleidungsstücke: display grid, grid-template-columns repeat(auto-fill, minmax(160px,1fr)), gap 16px. Rechte Spalte (Bühne/Preview): bg=surface_raised(#1E1E21), border 1px solid border_light, radius lg, padding 32px, position sticky top 88px, display flex, flex-direction column, align-items center, justify-content center. Preview-Fläche: w 280px, h 400px, bg=#0B0B0C, border 2px dashed border_light, radius md, display flex, align-items center, justify-content center. Leerer Zustand: color=fg_muted, text 'Ziehe Kleidungsstücke hierher'. Mobile (<768px): grid-template-columns 1fr, rechte Spalte als fixed bottom sheet (height 40vh, border-radius 24px 24px 0 0).

### Outfit-Galerie (Laufsteg horizontal)

Container: display flex, overflow-x auto, gap 24px, padding 32px 0, scroll-snap-type x mandatory, scrollbar styled (height 4px, thumb=accent, track=border). Jedes Outfit: flex 0 0 280px, scroll-snap-align start, bg=surface(#161618), border 1px solid border, radius lg, overflow hidden, transition all 250ms ease. Hover: border-color accent, box-shadow 0 12px 40px rgba(0,0,0,0.5), transform scale(1.02). Outfit-Bild: w 100%, h 320px, object-fit cover, bg=#1A1A1D. Outfit-Name: padding 16px, font_family heading, size lg, color=fg, text-align center. Mobile: flex 0 0 220px, gap 16px, padding 16px 0.

## Layout Principles

- Container max-width: 1280px, zentriert mit auto-margins, padding-x 24px (mobile: 16px)
- Breakpoints: mobile < 640px, tablet 640–1024px, desktop >= 1024px
- Grid: 12-Spalten CSS-Grid für Hauptlayouts, auto-fill für Garderoben-Karten
- Seiten-Hintergrund: durchgehend bg(#0B0B0C), kein Weißraum außerhalb des Containers
- Vertikaler Rhythmus: Sektionen durch 48px–64px Abstand getrennt, innerhalb von Sektionen 24px
- Gold-Akzent sparsam einsetzen: nur für interaktive Elemente, Überschriften-Highlights und Spotlight-Effekte – nicht für dekorative Flächen
- Burgunderrot ausschließlich für Badges, Danger-Buttons und subtile Flächen-Hintergründe (burgundy_surface)
- Alle interaktiven Flächen: min-tap-target 44×44px, focus-visible outline 2px gold
- Scrollbars global stylen: schmal (6px), dunkler Track (#1A1A1E), goldener Thumb
- Ladezustände: Skeleton-Screens mit pulsendem surface-Ton statt Spinner, shimmer-gradient mit accent-Anteil
