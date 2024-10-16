#digunakan unutk evaluasi murid berdasarkan performa
def evaluate_student_performance(percentage):

    #jika persentase lebih dari 90 akan ditampilkan Excellent performance
    if percentage >= 90:
        print("Excellent performance")

    #jika persentase lebih dari 80 akan ditampilkan Very Good performance
    elif percentage >= 80:
        print("Very Good performance")

    #jika persentase lebih dari 70 akan ditampilkan Good performance
    elif percentage >= 70:
        print("Good performance")

    #jika persentase lebih dari 60 akan ditampilkan Average performance
    elif percentage >= 60:
        print("Average performance")

    else:
        print("Poor performance")


student_percentage = float(input("Masukkan persentase siswa: "))

#cetak hasil peforma murid
evaluate_student_performance(student_percentage)
