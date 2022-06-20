# Things arised in the production environment --- Angular?

## Get ClipboardEvent paste value of input field

```html
<!-- xxx.HTML -->
<input (paste)="onPaste($event)" />
```

```ts
// xxx.TS
onPaste(event: ClipboardEvent) {
  const clipboardData = e.clipboardData || window.clipboardData;
  const pastedData = clipboardData.getData('Text');
  //...
}
```

## From FormGroup get Inner FormControl

```ts
FormGroup.get('FormControlName')?.value;
```

## Prevent +,-,e in number type input

```html
<!-- xxx.HTML -->
<input (keydown)="preventInvalidInput($event)" />
```

```ts
// xxx.TS
preventInvalidInput(event: KeyboardEvent) {
  const isZero = !this.filter.StakeholderIDs[0] && event.key === '0';
  if (['-', '+', 'e'].includes(event.key) || isZero) {
    event.preventDefault();
  }
}
```

## Angular animation

### Dropdown like

<iframe
  src="https://stackblitz.com/edit/animated-div-height?file=src%2Fapp%2Fapp.component.ts"
  style="width:100%; height:300px;"
></iframe>

### Delete and auto reset alignment

<iframe
  src="https://stackblitz.com/edit/angular-flex-animate-firefox?file=src%2Fapp%2Fapp.component.ts"
  style="width:100%; height:300px;"
></iframe>

### Sharing data between angular components four methods

<iframe
  src="https://fireship.io/lessons/sharing-data-between-angular-components-four-methods/"
  style="width:100%; height:500px;"
></iframe>
