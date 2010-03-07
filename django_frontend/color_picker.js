<html>
<head>
    <title>color picker tests</title>
    
    <script language="javascript" type="text/javascript" src="http://ajax.googleapis.com/ajax/libs/jquery/1.2.6/jquery.min.js"></script>
    <script language="javascript" type="text/javascript" src="jquery.colorPicker.js"/></script>
    
    <script type="text/javascript">
      //Run the code when document ready
      $(function() {    
       //use this method to add new colors to pallete
       //$.fn.colorPicker.addColors(['000', '000', 'fff', 'fff']);

       $('#color1').colorPicker();
       $('#color2').colorPicker();
       $('#color3').colorPicker(); 

       //fires an event when the color is changed
       //$('#color1').change(function(){
        //alert("color changed");
       //});

       $("#button1").click(function(){
        $("#color1").val("#ffffff");   
        $("#color1").change();
       });

       $("#button2").click(function(){
        $("#color2").val("#000000");   
        $("#color2").change();
       });

      });
    </script>

    <style type="text/css">
    /* styles adopted from Nidahas - Forms markup and CSS (http://nidahas.com/2006/12/06/forms-markup-and-css-revisited/) */
    /* General styles */
    body { margin: 0; padding: 0; font: 80%/1.5 Arial,Helvetica,sans-serif; color: #111; background-color: #FFF; }
    h2 { margin: 0px; padding: 10px; font-family: Georgia, "Times New Roman", Times, serif; font-size: 200%; font-weight: normal; color: #FFF; background-color: #CCC; border-bottom: #BBB 2px solid; }
    p#copyright { margin: 20px 10px; font-size: 90%; color: #999; }

    /* Form styles */
    div.form-container { margin: 10px; padding: 5px; background-color: #FFF; }

    p.legend { margin-bottom: 1em; }
    p.legend em { color: #C00; font-style: normal; }

    div.form-container div.controlset {display: block; float:left; width: 100%; padding: 0.25em 0;}

    div.form-container div.controlset label, 
    div.form-container div.controlset input,
    div.form-container div.controlset div { display: inline; float: left; }

    div.form-container div.controlset label { width: 100px;}

    </style>
    <link rel="stylesheet" href="colorPicker.css" type="text/css" />
    
    
</head>

<body>
    
    <h1>Let's get started.</h1>
    
    
    <p>Foo = {{ foo }} </p>
    <hr/>
    
    <div class="form-container">
    <form action="#" method="post">
    		<fieldset>
    			<div class="controlset"><label for="color1">Color 1</label> <input id="color1" type="text" name="color1" value="#333399" /></div>
    			<div class="controlset"><label for="color2">Color 2</label> <input id="color2" type="text" name="color2" value="#FF0000" /></div>
    			<div class="controlset"><label for="color3">Color 3</label> <input id="color3" type="text" name="color3" value="#99cc00" /></div>

    		</fieldset>

        <div class="buttonrow">
          <div><button type="button" id="button1">Set Color 1 to #FFF</button></div>
          <div><button type="button" id="button2">Set Color 2 to #000</button></div>
        </div>

    	</form>
    </div>
    
    
</body>
</html>
    