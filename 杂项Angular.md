# Things arised in the production environment --- Angular?

- [Get ClipboardEvent paste value of input field](#Get-ClipboardEvent-paste-value-of-input-field)

- [From FormGroup get Inner FormControl](#From-FormGroup-get-Inner-FormControl)

- [Prevent +,-,e in number type input](#Prevent--e-in-number-type-input)

- [Angular animation](#Angular-animation)

- [Dropdown like](#Dropdown-like)

- [Delete and auto reset alignment](#Delete-and-auto-reset-alignment)

- [Sharing data between angular components four methods](#Sharing-data-between-angular-components-four-methods)

- [Sanitization in angular](#Sanitization-in-angular)

- [Linkify link text to anchor tag](#Linkify-link-text-to-anchor-tag)

- [Set class name conditionally](#Set-class-name-conditionally)

- [Angular html divider](#Angular-html-divider)

- [Attribute/class selector component](#Attributeclass-selector-component)

- [Update Angular CLI in existing project](#Update-Angular-CLI-in-existing-project)

- [override css in `<mat-menu>`](#override-css-in-mat-menu)

- [Template accessibility of `@ViewChild` and `@ContentChild`](#Template-accessibility-of-ViewChild-and-ContentChild)

- [Angular Lifecycle Hooks](#Angular-Lifecycle-Hooks)

- [`MediaObserver`](#MediaObserver)

- [`ExpressionChangedAfterItHasBeenCheckedError`](#ExpressionChangedAfterItHasBeenCheckedError)

- [2-way Data Binding for customized component](#2-way-Data-Binding-for-customized-component)

- [Use localStorage in Angular](#Use-localStorage-in-Angular)

- [Custom tooltip follow cursor](#Custom-tooltip-follow-cursor)

- [Use renderer2 for class binding](#Use-renderer2-for-class-binding)

- [Flex-layout responsive API](#Flex-layout-responsive-API)

- [Image path in Angular](#Image-path-in-Angular)

- [`getElementsByClassName` and `querySelectorAll`](#getElementsByClassName-and-querySelectorAll)

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

[StackBlitz](https://stackblitz.com/edit/animated-div-height?file=src%2Fapp%2Fapp.component.ts)

### Delete and auto reset alignment

[StackBlitz](https://stackblitz.com/edit/angular-flex-animate-firefox?file=src%2Fapp%2Fapp.component.ts)

## Sharing data between angular components four methods

[More Info](https://fireship.io/lessons/sharing-data-between-angular-components-four-methods/)

## Sanitization in angular

[Bypass pipe](https://medium.com/@swarnakishore/angular-safe-pipe-implementation-to-bypass-domsanitizer-stripping-out-content-c1bf0f1cc36b)
[Angular doc](https://angular.io/api/platform-browser/DomSanitizer)

## Linkify link text to anchor tag

```ts
let cursor = 0;
const substrings = linkify
  .find(content)
  .map(({ href, value, start, end }, i, arr) => {
    let substring =
      content.slice(cursor, start) + '<a href="' + href + '">' + value + '</a>';
    cursor = end;
    if (arr.length - 1 === i) substring += content.slice(cursor);
    return substring;
  });

return substrings.length === 0 ? content : substrings.join('');
```

## Set class name conditionally

[Stack Overflow](https://stackoverflow.com/questions/35269179/angular-conditional-class-with-ngclass)

## Angular html divider

[Angular doc](https://material.angular.io/components/divider/overview)

## Attribute/class selector component

[Attribute selector \*](https://medium.com/javascript-everyday/when-to-use-an-attribute-selector-for-angular-components-7e788ba1bfe7)
[Selector as a Class](https://www.pluralsight.com/guides/understanding-the-purpose-and-use-of-the-selector-in-angular)

## Update Angular CLI in existing project

[Angular update guide](https://update.angular.io/)

e.g. 12->13

`npm i --force`
`npx @angular/cli@13 update @angular/core@13 @angular/cli@13`

## override css in `<mat-menu>`

```html
<!-- .html -->
<mat-menu #appMenu="matMenu" class="custom">
  <!-- menu stuff -->
</mat-menu>
```

```scss
::ng-deep .custom {
  //whatever your rules
}
```

## Template accessibility of `@ViewChild` and `@ContentChild`

`@ViewChild`: access in `ngAfterViewInit()`
`@ContentChild`: access `ng-content` template in child component, in `ngAfterContentChecked()`
`ngAfterContentChecked()`: Called after content (ng-content) has been projected into view

## Angular Lifecycle Hooks

![This is an image](/contents/images/lifecycleHooks.png)

## `MediaObserver`

Identifying breakpoints and Media Queries

```ts
//can be use to get break points on viewports change
columnsByBreakpoint = {
  xl: 14,
  lg: 9,
  md: 6,
  sm: 4,
  xs: 2,
};
```

## `ExpressionChangedAfterItHasBeenCheckedError`

[Causes](https://angular.io/errors/NG0100)

Solution:

```ts
this.cdRef.detectChanges();
```

[Stack Overflow](https://stackoverflow.com/questions/39787038/how-to-manage-angular2-expression-has-changed-after-it-was-checked-exception-w/39787056#39787056)

## 2-way Data Binding for customized component

[More Info](https://blog.thoughtram.io/angular/2016/10/13/two-way-data-binding-in-angular-2.html)

## Use localStorage in Angular

[More Info](https://medium.com/@nixonaugustine5/localstorage-and-sessionstorage-in-angular-app-65cda19283a0)

## Custom tooltip follow cursor

[Plnkr](https://plnkr.co/edit/8p02DDId5ysgRnkgoSBT?preview)

```ts
app.directive('tooltipFollowCursor', function () {
  return {
    restrict: 'A',
    link: function (scope, element, attrs) {
      var x, y;
      element.on('mousemove', function (e) {
        (x = e.pageX), (y = e.pageY);
        this.children[0].style.top = y + 15 + 'px';
        this.children[0].style.left = x + 15 + 'px';
      });
    },
  };
});
```

## Use renderer2 for class binding

[StackBlitz](https://stackblitz.com/edit/angular-2qtml4?file=src%2Fapp%2Fapp.component.ts)

## Flex-layout responsive API

[Github](https://github.com/angular/flex-layout/blob/master/docs/documentation/Responsive-API.md)

## Image path in Angular

No need relative path, just use `assets/...`

```html
<img src="assets/img.jpg" alt="" />
```

[More Info](https://mdbootstrap.com/support/angular/images-not-loading-from-assets-folder-in-angular/#:~:text=You're%20using%20the%20wrong,.%2F..%2Fassets.)

## `getElementsByClassName` and `querySelectorAll`

`getElementsByClassName` returns live collection (HTMLcollection)

`querySelectorAll` returns static collection (NodeList)

[More Info](https://stackoverflow.com/questions/14377590/queryselector-and-queryselectorall-vs-getelementsbyclassname-and-getelementbyid/39213298#39213298)
