while read dirname; do
  cd "${dirname}"
	git log -p &> "${dirname}"_diff
	mv "${dirname}"_diff ../diffs
	cd ..
	rm -rf "${dirname}"
done < repository_names_2
