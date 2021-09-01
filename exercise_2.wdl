
version 1.0
task pythonaddition {
    input {
        Int operand_one
        Int operand_two
        File script
    }
    command {
        python3 ${script} --operand1 ${operand_one} --operand2 ${operand_two} > results.txt
    }
    output {
        File result = "results.txt"
    }
}

workflow testing {
    call pythonaddition as addition {
    }
}