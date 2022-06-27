# Things arised in the production environment --- HTML?CSS?

## Hide sibling div on hover with css

[Stack Overflow](https://stackoverflow.com/questions/38084539/hide-sibling-div-on-hover-with-css-only)

## How to make overflow not exceed parents element's padding

Issue:

- CSS `overflow: hidden` makes the child element hide after overflowing the parent element
- But the padding is part of the parent element, so overflow into the padding does not count as overflow parent element
- Thus overflow will not hide in padding

Solution:

- Wrap it with another element and make that element `overflow: hidden`
- The original parent element padding will be apply to the wrap element, and - the inner element won't exceed the wrap element

## Flex-basis Flex-shrink Flex-grow

[YouTube](https://www.youtube.com/embed/LVLmX-fx09w)

## Capitalize the First Letter of Each Word

[More Info](https://www.freecodecamp.org/news/how-to-capitalize-words-in-javascript/)

## ::after ::before

[CSS tricks](https://css-tricks.com/almanac/selectors/a/after-and-before/)

## Absolute Horizontal And Vertical Centering In CSS

```scss
.Absolute-Center {
  margin: auto;
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
}
```

[More Info](https://www.smashingmagazine.com/2013/08/absolute-horizontal-vertical-centering-css/)

## CSS filter generator to convert from black to target hex color

[More Info](https://codepen.io/sosuke/pen/Pjoqqp)
