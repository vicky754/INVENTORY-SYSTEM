#!python
print("content-type: text/html\r\n\r\n")

content='''
    <!DOCTYPE html>
	<html>
		<head>
			<title>Alpha In Detail</title>
			<link rel="stylesheet" type="text/css" href="/alpha/css/alphain.css">
		</head>
		<body>
			<div class="panel">
				<p>Depot In Details</p>
			</div>
			<div class="logo">
				
			</div>
			<h1>Majesty Marine Services</h1>
				<div class="alphain">
					<h2>Alpha Omega Shipping Services PVT LTD</h2>

						<form action="/cgi-bin/alpha/alphain.py" method="post" id="alphain">

								
							
							<a href="depo.py" class="link">Back</a><br><br>
                        
							<div class="box">
							<label for="Line Name">Line Name</label><br>
							<input type="text" name="lname" id="lname" placeholder="Enter Line Name"/><br><br>
							</div>
							
							<div class="box">
							<label for="Refrence Number">Refrence number</label><br>
							<input type="text" name="ref" id="ref-num" placeholder="Enter Refrence number"/><br><br>
							</div>
							
							<div class="box">
							<label for="In Date">In Date</label><br>
							<input type="date" name="indate" id="in-date" placeholder=""/><br><br>
							</div>
	
							<div class="clear"></div>
							
							<div class="box">
							<label for="Container number">Container Number</label><br>
							<input type="text" name="container" id="cont" placeholder="eg: @abcd1234567" maxlength="11" required/><br><br>
							</div>
							
							<div class="box">
							<label for="Size">Size</label><br>
                                <input id="size" type="number" name="size" placeholder="eg: 20" maxlength="2"/><br><br>
							</div>
                            
                            <div class="box">
							<label for="Type">Type</label><br>
                                <input id="type" type="text" name="type" placeholder="eg: DV" maxlength="2"/><br><br>
							</div>
							
							 <div class="clear"></div>

							<div class="box">
							<label for="transporter">transporter Name</label><br>
							<input type="text" name="transporter" id="trans" placeholder="Enter transporter Name"/><br><br>
							</div>
                           

							<div class="box">
							<label for="Vehicle Number">Vehicle Number</label><br>
							<input type="text" name="vehicle" id="vehicle" placeholder="eg: MH123456"/><br><br>
							</div>

							<div class="box">
							<label for="From">Come From</label><br>
							<input type="text" name="from" id="from" placeholder="eg: @PUNE"/><br><br>
							</div>

							<div class="clear"></div>

							<div class="box">	
							<label for="Party Name">Party Name</label><br>
							<input type="text" name="party" id="party" placeholder="Enter Party Name"/><br><br>
							</div>
								
							<div class="box">
							<label for="Valid Date">Valid Date</label><br>
							<input type="date" name="vdate" id="v-date" placeholder=""/><br><br>
							</div>
							
							<div class="box">
							<label for="Cash">Cash Collection</label><br>
							<input type="number" name="cash" id="cash" placeholder="eg: Rs-"/><br><br>
							</div>

							<div class="clear"></div>

							<div class="box">					
							<label for="Remark">Remark</label><br>
							<input type="text" name="remark" id="remark" placeholder="" /><br><br>
							</div>

                            <div class="clear"></div>

							
							
							<input type="submit" name="Enter" value="In Container" id="enter"/>
						
						
						
						</form>
				</div>
		</body>
	</html>

'''

print(content)