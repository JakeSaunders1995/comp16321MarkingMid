// MU0 ALU testbench
// P W Nutter (based on a design by Jeff Pepper)
// Date 7/7/2021

// #1 = 1ns
`timescale 1ns/100ps

// module header

module mu0_alu_tb();

// Define any internal connections required

reg [15:0]  X,
reg [15:0]  Y,
reg [1:0]   M,
wire [15:0]  Q);


// Instantiate device under test

mu0_alu dut (X, Y, M, Q)


// Test vectors
initial
begin
// There are 10 tests described below. Please provide the appropriate
// values for the inputs that will implement the required test for each.


// Provide test stimulus to confirm that a negative value is passed through
// on the Y input to the MUX for the passthrough operation

#100 M = 2b'00; X = 16b'h0001; Y 16b'hF001;

// Provide test stimulus for a SUB operation that when one input is
// 10 (in decimal) a value of 0 is observed at the output

#100 M = 2b'11; X = 16b'd0001; Y 16b'd0001;

// Provide test stimulus that when ADDing two positive values results
// in a negative result being observed

#100 M = 2b'01; X = 16b'h0001; Y 16b'h1002;

// Provide test stimulus that will result in an address of 00FE being
// generated in the fetch phase

#100 M = 2b'00; X = 16b'h0001; Y 16b'h00FE;

// Provide non-zero test stimulus that will result is a result of zero
// being observed for and ADD operation

#100 M = 2b'01; X = 16b'hE001; Y 16b'h1FFF;

// Provide test stimulus for a SUB operation that will produce a result
// of -1

#100 M = 2b'11; X = 16b'h0001; Y 16b'h0002;

// Produce test stimulus that will produce a result of 0FFF for
// the passthrough operation

#100 M = 2b'00; X = 16b'h0001; Y 16b'h0FFF;

// Produce test stimulus that will result in an output of 0 for
// the increment operation

#100 M = 2b'01; X = 16b'hE001; Y 16b'h1FFF;

// Produce test stimulus that generates a result of 0FF0 for a
// SUB operation when one of the inputs is 000F

#100 M = 2b'11; X = 16b'h000F; Y 16b'hFE1;

// Produce test stimulus for an ADD operation that for two
// negative values generates a positive result

#100 M = 2b'01; X = 16b'hE001; Y 16b'h1FFF;

  #100 $finish;   // end the simulation
end

// Save results as VCD file
// Do not change
initial
 begin
  $dumpfile("mu0_alu_tb_results.vcd");  // Save simulation waveforms in this file
  $dumpvars; // Capture all simulation waveforms
 end

endmodule
