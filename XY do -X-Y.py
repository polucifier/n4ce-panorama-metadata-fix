def negate_xy_in_files(nazev,pocet_souboru):
    nazev = nazev[:-9]
    for i in range(1, pocet_souboru+1):  # From 1 to n inclusive
        track_number = f"{i:02d}"  # Pad with zeros: 01, 02, ..., 21
        input_filename = f"{nazev}{track_number}_Sphere.csv"
        output_filename = f"output_{nazev}{track_number}.csv"

        try:
            with open(input_filename, 'r') as f_in, open(output_filename, 'w') as f_out:
                for line in f_in:
                    parts = line.strip().split(';')
                    if len(parts) > 4:
                        # Negate Y (index 2) and X (index 3)
                        y = -float(parts[2])
                        x = -float(parts[3])
                        r1 = -float(parts[8])
                        r2 = -float(parts[9])
                        r3 = -float(parts[10])
                        r4 = -float(parts[11])
                        r5 = -float(parts[12])
                        r6 = -float(parts[13])
                        parts[2] = f"{y:.10f}"
                        parts[3] = f"{x:.10f}"
                        parts[8] = f"{r1:.10f}"
                        parts[9] = f"{r2:.10f}"
                        parts[10] = f"{r3:.10f}"
                        parts[11] = f"{r4:.10f}"
                        parts[12] = f"{r5:.10f}"
                        parts[13] = f"{r6:.10f}"

                        f_out.write(';'.join(parts) + '\n')
                    else:
                        f_out.write(line)

            print(f"Processed: {input_filename} → {output_filename}")

        except FileNotFoundError:
            print(f"File not found: {input_filename} (Skipping)")

# Run the function
negate_xy_in_files("Job_20240108_1012_Track01_Sphere", 21)
