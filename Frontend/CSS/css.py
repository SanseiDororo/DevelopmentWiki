import streamlit as st

def css():
    st.header('CSS')
    st.write("")
    st.write('''
            
        This section covers most importan aspects of the CSS. The content is divided into
        topics such as properties, steps, examples. Detailed explanation of each topic is 
        provided in the extensions below. 


            ''')
    
    st.write(''' ''')
    st.write(''' ''')

    with st.expander('Box Sizing'):
        st.write(
            '''
            Box Sizing a CSS property that defines how the total width and height of an element is calculated. It affects the sizing of an element's content box and any padding and border that is applied to the element.
            The box-sizing property can have two values:

            * content-box: This is the default value, where the total width and height of an 
            element is calculated based on the width and height of the element's content box. 
            Any padding or border that is applied to the element is added to the width and height 
            of the element.

            * border-box: With this value, the total width and height of an element 
            is calculated based on the width and height of the element's border box. 
            This includes any padding or border that is applied to the element. The 
            element's content box is then calculated by subtracting the padding and 
            border from the total width and height.
            

            Example:

            ```
            .box {
              width: 200px;
              height: 100px;
              padding: 10px;
              border: 1px solid black;
              box-sizing: border-box;
            }
            ```
            In this example, the box-sizing property is set to border-box, so the total 
            width and height of the .box element will be 200px x 100px, including the padding 
            and border. The content box will be 178px x 78px, since 22px (10px padding + 2px border 
            on each side) is taken up by the padding and border.

            Using box-sizing: border-box can be useful in certain situations, such as 
            when you want to specify a fixed width or height for an element that includes 
            padding and border. It can also help to simplify layout calculations and make your 
            styles more predictable.
            '''
            )
        
    with st.expander('VH'):
        st.write(
            r'''
            The vh unit represents 1% of the height of the viewport. The viewport is the 
            user's visible area of a web page. It varies with the device, and will be smaller 
            on a mobile phone than on a computer screen.

            Example:

            ```
            .box {
              width: 100vh;
              height: 100vh;
              background: red;
            }
            ```
            '''
        )

    with st.expander('Image Properties'):
        st.write(
            '''

            ###### Image Size

            The image properties allow you to control the size and alignment of an image. 
            The width and height properties control the size of the image. The max-width 
            and max-height properties control the maximum size of the image. The min-width 
            and min-height properties control the minimum size of the image. The object-fit 
            property controls how the image fills its container. The object-position property 
            controls the alignment of the image within its container. The image-orientation 
            property controls the orientation of the image.

            Example:

            ```
            .box {
                width: 100px;
                height: 100px;
                background: url("img_tree.png") no-repeat center center;
                background-size: cover;
            }
            ```
            ---
            ###### Gradient

            The gradient property is used to create a gradient effect on an element.

            The gradient property can take different types of values, including:

            * Linear gradients (e.g., to bottom, to right, to bottom right, to top right,
            to bottom left, to top left, to right top, to left bottom, to right bottom, to left top)
            to create a linear gradient effect.

            * Radial gradients (e.g., circle, ellipse) to create a radial gradient effect.

            * Multiple values (e.g., linear-gradient(red, blue), radial-gradient(red, blue))
            to create multiple gradient effects.

            Example:

            ```
                background-image:linear-gradient(
                to right bottom,
                hsla(111, 55%, 64%, 0.8),
                hsla(160, 64%, 43%, 0.80)),
                url(../img/hero.jpg);
            ```


            ---

            ###### Background-size

            The background-size property specifies the size of the background images.

            The background-size property can take different types of values, including:

            * Length values (e.g., px, em, %) to specify the width and height 
            of the background image in pixels, ems or percentages.

            * Keyword values (auto, contain, cover) to automatically 
            adjust the size of the background image. auto sets the size to the intrinsic size of the image. contain scales the image to fit within the container while maintaining its aspect ratio. cover scales the image to cover the entire container while maintaining its aspect ratio.

            * Multiple values (e.g., width height, auto height, cover auto) to specify 
            both the width and height of the background image independently.

            Example:

            ```
                background-size: cover;
            ```

            ---

            ###### Background-position

            The background-position property specifies the position of the background image.

            The background-position property can take different types of values, including:
            top, bottom, left, right, center, and percentages.

            * top: The background image is placed at the top of the element.
            * bottom: The background image is placed at the bottom of the element.
            * left: The background image is placed to the left of the element.
            * right: The background image is placed to the right of the element.
            * center: The background image is centered both horizontally and vertically within the element.
            * percentages: The background image is placed according to the percentage specified. The first value is the horizontal position and the second value is the vertical position. The first value represents the left position and the second value represents the top position.
            *
            
            Example:

            ```
                background-position: center;
            ```


            



        
        '''
        )

    with st.expander('Initial state'):
        st.write(
            '''
            Though browsers have their own default styles, it is a good practice to
            explicitly set the initial state of all elements. This is done by setting
            all the properties to their initial values. This is done by using the
            universal selector * and the initial keyword.

            Example:
            
            ```
            * {
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }
            ```
            '''
        )

   
    with st.expander('Fonts'):
        st.write(
            '''
            We need to include the font we want to use in our project. There are two ways to do this:

            * Using a link tag in the head of our HTML file. This is the most common way to include 
            fonts in a project. We can use the Google Fonts service to find the font we want to use 
            and then include it in our project by adding a link tag to the head of our HTML file. 
            The link tag will look something like this:

            ```
            <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@100;300;400;500;700;900&display=swap" rel="stylesheet">
            ```
            * Using the @font-face rule. This is a CSS rule that allows us to include a 
            font in our project. We can use the @font-face rule to include a font that is 
            not available on Google Fonts. The @font-face rule will look something like this:

            ```
            @font-face {
                font-family: 'Roboto';
                font-style: normal;
                font-weight: 100;
                src: local('Roboto Thin'), local('Roboto-Thin'), url(https://fonts.gstatic.com/s/roboto/v20/KFOkCnqEu92Fr1MmgVxIIzIXKMnyrYk.woff2) format('woff2');
                unicode-range: U+0102-0103, U+1EA0-1EF9, U+20AB;
            }
            ```

            Once we have included the font in our project, we can use it in our CSS by setting 
            the font-family property to the name of the font. For example, if we want to use the 
            Roboto font in our project, we can set the font-family property to Roboto.

            We usually set the font-family property on the body element, so that all the text
            in our project will use the font we have specified. We can also set the font-family
            property on individual elements to override the font-family property on the body element.

            Example:

            ```
            body {
                font-family: 'Roboto', sans-serif;
            }
            `https://www.youtube.com/watch?v=L3BFgB47pTU``

            The font-family property can have multiple values. The first value is the name of the
            font we want to use. The second value is a fallback font. If the first font is not
            available, the browser will use the fallback font. The fallback font can be any font
            that is available on the user's computer. The fallback font can also be a generic font
            family, such as serif, sans-serif, monospace, cursive, or fantasy.

            '''
            )

    with st.expander('Class selector'):
        st.write(
            '''
            The class selector selects elements with a specific class attribute. To select elements
            with a specific class, we add a period (.) before the name of the class. For example,
            to select all elements with the class "container", we can use the class selector like this:

            ```
            .container {
                width: 100%;
                height: 100%;
                background-color: #000;
            }
            ```

            We can also select multiple elements with the same class by separating the class names
            with a comma. For example, to select all elements with the class "container" and the
            class "main", we can use the class selector like this:

            ```
            .container, .main {
                width: 100%;
                height: 100%;
                background-color: #000;
            }
            ```

            '''
            )
        
    with st.expander('ID selector'):
        st.write(
            '''
            The ID selector selects elements with a specific ID attribute. To select elements
            with a specific ID, we add a hash (#) before the name of the ID. For example,
            to select the element with the ID "container", we can use the ID selector like this:

            ```
            #container {
                width: 100%;
                height: 100%;
                background-color: #000;
            }
            ```

            We can only select one element with a specific ID. If we try to select multiple
            elements with the same ID, only the first element will be selected. For example,
            if we have two elements with the ID "container", only the first element will be
            selected.

            '''
            )
        
    with st.expander('Pseudo-classes'):
        st.write(
            '''
            Pseudo-classes are used to define the style of an element based on a state. For example,
            we can use the :hover pseudo-class to define the style of an element when the user
            hovers over it with the mouse.

            Example:

            ```
            a:hover {
                color: #fff;
            }
            ```

            We can also use the :active pseudo-class to define the style of an element when the
            user clicks on it.

            Example:

            ```
            a:active {
                color: #fff;
            }
            ```

            '''
            )           
    with st.expander('Pseudo-elements'):
        st.write(
            '''
            Pseudo-elements are used to style a part of an element. For example, we can use the
            ::before pseudo-element to insert content before an element.

            Example:

            ```
            h1::before {
                content: 'Hello';
            }
            ```

            We can also use the ::after pseudo-element to insert content after an element.

            Example:

            ```
            h1::after {
                content: 'World';
            }
            ```

            '''
            )   
    with st.expander('Attribute selector'):
        st.write(
            '''
            The attribute selector selects elements with a specific attribute. To select elements
            with a specific attribute, we add a square bracket ([ ]) before the name of the attribute.
            For example, to select all elements with the attribute "href", we can use the attribute
            selector like this:
                
                ```
                [href] {
                    color: #fff;
                }
                ```
            We can also select elements with a specific attribute value by adding an equals sign
            (=) after the attribute name and then specifying the attribute value. For example, to
            select all elements with the attribute "href" that has the value "https://www.google.com",
            we can use the attribute selector like this:
                
                ```
                [href="https://www.google.com"] {
                    color: #fff;
                }
                ```
            We can also select elements with a specific attribute value that starts with a specific
            string by adding a caret (^) after the attribute name and then specifying the string.
            For example, to select all elements with the attribute "href" that starts with the
            string "https://", we can use the attribute selector like this:
                    
                    ```
                    [href^="https://"] {
                        color: #fff;
                    }
                    ```
            We can also select elements with a specific attribute value that ends with a specific
            string by adding a dollar sign ($) after the attribute name and then specifying the
            string. For example, to select all elements with the attribute "href" that ends with
            the string ".com", we can use the attribute selector like this:
                        
                ```
                [href$=".com"] {
                    color: #fff;
                }
                ```
            We can also select elements with a specific attribute value that contains a specific
            string by adding an asterisk (*) after the attribute name and then specifying the
            string. For example, to select all elements with the attribute "href" that contains
            the string "google", we can use the attribute selector like this:
                                
                    ```
                    [href*="google"] {
                        color: #fff;
                    }
                    ```
                '''
            )  
    
    with st.expander('Combinators'):
        st.write(
            '''
            Combinators are used to select elements based on their relationship to other elements.
            There are three different combinators in CSS: the descendant combinator, the child
            combinator, and the adjacent sibling combinator.

            The descendant combinator selects elements that are descendants of a specified element.
            To select elements that are descendants of a specified element, we separate the selectors
            with a space. For example, to select all p elements that are descendants of a div element,
            we can use the descendant combinator like this:
                
                ```
                div p {
                    color: #fff;
                }
                ```
            The child combinator selects elements that are children of a specified element. To select
            elements that are children of a specified element, we separate the selectors with a greater
            than sign (>). For example, to select all p elements that are children of a div element,
            we can use the child combinator like this:
                
                ```
                div > p {
                    color: #fff;
                }
                ```
            The adjacent sibling combinator selects elements that are the next sibling of a specified
            element. To select elements that are the next sibling of a specified element, we separate
            the selectors with a plus sign (+). For example, to select all p elements that are the
            next sibling of a div element, we can use the adjacent sibling combinator like this:
                
                ```
                div + p {
                    color: #fff;
                }
                ```
            '''
            )
    
    with st.expander('Positioning'):
        st.write(
            '''
            Positioning is used to control the layout of elements. There are four different types
            of positioning in CSS: static, relative, absolute, and fixed.

            The static positioning is the default positioning. An element with static positioning
            is not affected by the top, right, bottom, and left properties.

            The relative positioning is similar to the static positioning, except an element with
            relative positioning is positioned relative to its normal position. An element with
            relative positioning is affected by the top, right, bottom, and left properties.

            The absolute positioning is positioned relative to the nearest positioned ancestor
            (instead of positioned relative to the viewport, like fixed). However; if an absolute
            positioned element has no positioned ancestors, it uses the document body, and moves
            along with page scrolling. An element with absolute positioning is affected by the
            top, right, bottom, and left properties.

            The fixed positioning is positioned relative to the viewport, which means it always
            stays in the same place even if the page is scrolled. An element with fixed positioning
            is affected by the top, right, bottom, and left properties.

            Example:

            ```
            .container {
                position: relative;
                width: 100%;
                height: 100%;
                background-color: #000;
            }
            ```
            '''
            )
    with st.expander('Display'):
        st.write(
            '''
            The display property specifies the display behavior (the type of rendering box) of an element.

            The display property can have one of the following values:

            * block: The element generates a block element box. Default for most elements.
            * inline: The element generates one or more inline element boxes which
            takes minimum space (default for <span>)
            * inline-block: The element generates one or more inline element boxes that are formatted 
            as block boxes. They combine the features of both inline and block-level elements. This means
            that element takes minimal space but can have height and width properties.
            * list-item: The element generates a block box that will be laid out as a list item.
            * flex: The element generates a block-level flex container box.
            * inline-flex: The element generates an inline-level flex container box
            * grid: The element generates a block-level grid container box.
            * inline-grid: The element generates an inline-level grid container box.
            * table: The element generates a block-level table box.
            * inline-table: The element generates an inline-level table box.
            * none: The element does not generate any box.
            ()

            Example:

            ```
            .container {
                display: block;
            }
            ```
            '''
            )
        
    with st.expander('Flex Box'):\
        st.write('''
            Flexbox is a one-dimensional layout method for laying out items in rows or columns.
            Flexbox is a great tool for creating responsive layouts. 

            Flex box has two main axes: the main axis and the cross axis. The main axis is the
            primary axis along which flex items are laid out. The cross axis runs perpendicular
            to the main axis. The main axis direction is defined by the flex-direction property,
            and the cross axis direction is defined by the flex-direction property.

            The flex-direction property specifies the direction of the main axis. It can have
            one of the following values:

            * row: The main axis is defined to be the same as the text direction. The main start
            and main end points are the same as the content direction.
            * row-reverse: The main axis is defined to be the same as the text direction. The main
            start and main end points are the same as the opposite of the content direction.
            * column: The main axis is defined to be perpendicular to the text direction. The main
            start and main end points are the same as the content direction.
            * column-reverse: The main axis is defined to be perpendicular to the text direction.
            The main start and main end points are the same as the opposite of the content direction.

            Example:

            ```
            .container {
                display: flex;
                flex-direction: row;
            }
            ```
            ---

            The flex-wrap property specifies whether flex items are forced into a single line or
            can be wrapped onto multiple lines. It can have one of the following values:

            * nowrap: The flex items are not wrapped. The flex container is one single line.
            * wrap: The flex items are wrapped onto multiple lines. The direction of the wrap is
            defined by the flex-direction property.
            * wrap-reverse: The flex items are wrapped onto multiple lines. The direction of the
            wrap is the opposite of the direction defined by the flex-direction property.

            Example:

            ```
            .container {
                display: flex;
                flex-wrap: wrap;
            }
            ```

            ---

            The justify-content property specifies the alignment along the main axis. It can have
            one of the following values:

            * flex-start: The flex items are packed toward the start of the flex container.
            * flex-end: The flex items are packed toward the end of the flex container.
            * center: The flex items are centered along the main axis.
            * space-between: The flex items are evenly distributed in the flex container. The first
            flex item is flushed to the start of the container, and the last flex item is flushed
            to the end of the container.
            * space-around: The flex items are evenly distributed in the flex container with equal
            space around them.
            * space-evenly: The flex items are distributed so that the spacing between any two
            adjacent items is the same.

            Example:

            ```
            .container {
                display: flex;
                justify-content: space-between;
            }
            ```
            ---

            The align-items property specifies the alignment along the cross axis. It can have
            one of the following values:
            
            * stretch: The flex items are stretched to fill the container.
            * flex-start: The flex items are packed toward the start of the cross axis.
            * flex-end: The flex items are packed toward the end of the cross axis.
            * center: The flex items are centered along the cross axis.
            * baseline: The flex items are aligned such as their baselines align.

            Example:

            ```
            .container {
                display: flex;
                align-items: center;
            }
            ```
            --- 

            The align-content property specifies the alignment along the cross axis when there
            is extra space in the cross-axis. It can have one of the following values:

            * stretch: The flex items are stretched to fill the container.
            * flex-start: The flex items are packed toward the start of the cross axis.
            * flex-end: The flex items are packed toward the end of the cross axis.
            * center: The flex items are centered along the cross axis.
            * space-between: The flex items are evenly distributed in the flex container. The first
            flex item is flushed to the start of the container, and the last flex item is flushed
            to the end of the container.

            Example:

            ```
            .container {
                display: flex;
                align-content: center;
            }
            ```
            --- 

            The order property specifies the order of the flex item, relative to the rest of the
            flex items inside the same container. Items are ordered by ascending order. The order
            property has no effect on the order of the flex items if the flex-direction property
            is set to row or row-reverse.

            Example:

            ```
            .container {
                display: flex;
                order: 1;
            }
            ```
            --- 

            The flex-grow property specifies how much the flex item will grow relative to the rest
            of the flex items inside the same container. The flex-grow property has no effect if
            the flex-direction property is set to row or row-reverse.

            Example:

            ```
            .container {
                display: flex;
                flex-grow: 1;
            }
            ```
            ---

            The flex-shrink property specifies how much the flex item will shrink relative to the
            rest of the flex items inside the same container. The flex-shrink property has no
            effect if the flex-direction property is set to row or row-reverse.
            
            Example:

            ```
            .container {
                display: flex;
                flex-shrink: 1;
            }
            ```
            ---
            The flex-basis property specifies the initial length of a flex item. The flex-basis
            property has no effect if the flex-direction property is set to row or row-reverse.

            Example:

            ```
            .container {
                display: flex;
                flex-basis: 100px;
            }
            ```
            ---
            The flex property is a shorthand property for the flex-grow, flex-shrink, and
            flex-basis properties.

            Example:

            ```
            .container {
                display: flex;
                flex: 1 1 100px;
            }
            ```
            ---
            The align-self property specifies the alignment for the selected item inside the
            flexible container. The align-self property overrides the align-items property.

            Example:

            ```
            .container {
                display: flex;
                align-self: center;
            }
            ```
            ---
            The flex-flow property is a shorthand property for the flex-direction and flex-wrap
            properties.

            Example:

            ```
            .container {
                display: flex;
                flex-flow: row wrap;
            }
            ```

            [Visual Explanation](https://css-tricks.com/snippets/css/a-guide-to-flexbox/)

        ''')
    
    with st.expander('CSS Grid'):
        st.write('''
            The CSS Grid Layout Module offers a grid-based layout system, with rows and columns,
            making it easier to design web pages without having to use floats and positioning.
            The grid layout is defined by a parent element, with one or more child elements.
            The child elements are placed into the grid layout by defining a grid item for each
            element.

            Constructing the grid:

            * The grid container is defined with the display property set to grid or inline-grid.
            * The grid container is defined with grid-template-columns, grid-template-rows,
            grid-template-areas, grid-template, grid-auto-columns, grid-auto-rows, grid-auto-flow,
            or grid properties.
            * The grid items are placed into the grid by defining a grid area for each item.

            Example:

            ```
            .container {
                display: grid;
                grid-template-columns: repeat(3, 1fr);
                grid-template-rows: repeat(3, 1fr);
            }
            ```
            ---

            The grid-template-columns property defines the columns of the grid with a space-separated
            list of values. The values represent the track size, and the space between them represents
            the grid line.

            Example:

            ```
            .container {
                display: grid;
                grid-template-columns: 50px 50px 50px;
            }
            ```
            ---

            The grid-template-rows property defines the rows of the grid with a space-separated list
            of values. The values represent the track size, and the space between them represents
            the grid line.

            Example:

            ```
            .container {
                display: grid;
                grid-template-rows: 50px 50px 50px;
            }
            ```
            ---
            The grid-template-areas property defines a grid template by referencing the names of the
            grid areas which are specified with the grid-area property.

            Example:

            ```
            .container {
                display: grid;
                grid-template-areas: "header header header"
                                        "main main ."
                                        "footer footer footer";
            }

            .item1 {
                grid-area: header;
            }

            .item2 {
                grid-area: main;
            }

            .item3 {
                grid-area: footer;
            }
            ```
            ---
            The grid-template property is a shorthand property for the grid-template-rows,
            grid-template-columns, and grid-template-areas properties.

            Example:
            
            ```
            .container {
                display: grid;
                grid-template: 50px 50px 50px / 50px 50px 50px;
            }
            ```

            ---

            The grid-auto-columns property specifies the size of an implicitly-created column track.

            Example:

            ```
            .container {
                display: grid;
                grid-auto-columns: 50px;
            }
            ```

            ---

            The grid-auto-rows property specifies the size of an implicitly-created row track.

            Example:   

            ```
            .container {
                display: grid;
                grid-auto-rows: 50px;
            }
            ```
            ---

            The grid-auto-flow property specifies how auto-placed items are inserted in the grid.

            Example:
            
            ```
            .container {
                display: grid;
                grid-auto-flow: column;
            }
            ```

            ---

            The grid property is a shorthand property for the grid-template-rows, grid-template-columns,
            grid-template-areas, grid-auto-rows, grid-auto-columns, and grid-auto-flow properties.

            Example:

            ```
            .container {
                display: grid;
                grid: 50px 50px 50px / 50px 50px 50px;
            }
            ```
            ---

            The grid-column-start property specifies the line where the item should start.

            Example:

            ```
            .item1 {
                grid-column-start: 1;
            }
            ```

            ---

            The grid-column-end property specifies the line where the item should end.

            Example:

            ```
            .item1 {
                grid-column-end: 4;
            }
            ```

            ---

            The grid-row-start property specifies the line where the item should start.

            Example:

            ```
            .item1 {
                grid-row-start: 1;
            }
            ```

            ---

            The grid-row-end property specifies the line where the item should end.

            Example:

            ```
            .item1 {
                grid-row-end: 4;
            }
            ```

            ---

            The grid-column property is a shorthand property for the grid-column-start and
            grid-column-end properties.

            Example:

            ```
            .item1 {
                grid-column: 1 / 4;
            }
            ```
            ---

            The grid-row property is a shorthand property for the grid-row-start and grid-row-end
            properties.

            Example:

            ```
            .item1 {
                grid-row: 1 / 4;
            }
            ```

            ---

            The grid-area property specifies a name for the grid item, and a grid area where it
            should be placed.

            Example:

            ```
            .item1 {
                grid-area: header;
            }
            ```

            ---

            The justify-items property aligns grid items along the inline (row) axis (as opposed
            to align-items which aligns along the block (column) axis). This value applies to all
            grid items inside the container.

            Example:

            ```
            .container {
                display: grid;
                justify-items: center;
            }
            ```

            ---

            The align-items property aligns grid items along the block (column) axis (as opposed
            to justify-items which aligns along the inline (row) axis). This value applies to all
            grid items inside the container.

            Example:

            ```
            .container {
                display: grid;
                align-items: center;
            }
            ```

            ---

            The place-items property is a shorthand property for the align-items and justify-items
            properties.

            Example:

            ```
            .container {
                display: grid;
                place-items: center;
            }
            ```

            ---

            The justify-self property aligns a grid item inside a cell along the inline (row)
            axis. This value applies to a grid item inside a single cell.

            Example:

            ```
            .item1 {
                justify-self: center;
            }
            ```
            
            ---

            The align-self property aligns a grid item inside a cell along the block (column)
            axis. This value applies to a grid item inside a single cell.

            Example:

            ```
            .item1 {
                align-self: center;
            }
            ```

            ---

            The place-self property is a shorthand property for the align-self and justify-self
            properties.

            Example:

            ```
            .item1 {
                place-self: center;
            }
            ```

            ---

            The justify-content property aligns a grid container's content along the inline (row)
            axis. The inline (row) axis is defined to be the same as the block (column) axis of 
            the containing block.

            Example:

            ```
            .container {
                display: grid;
                justify-content: center;
            }
            ```

            ---

            The align-content property aligns a grid container's content along the block (column)
            axis. The block (column) axis is defined to be the same as the inline (row) axis of
            the containing block.

            Example:

            ```
            .container {
                display: grid;
                align-content: center;
            }

            ```

            ---

        ''')
    
        
        
