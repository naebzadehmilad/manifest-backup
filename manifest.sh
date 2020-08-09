i=(svc deploy pv pvc statful cm)
 for i in ${i[@]}; do
        kubectl get $i --all-namespaces -o yaml > $i
done
