import { Component, OnInit, Input } from '@angular/core';
import { Location } from '@angular/common';

import { Record } from '../record';
import { RecordService } from '../record.service';

@Component({
  selector: 'app-record-add',
  templateUrl: './record-add.component.html',
  styleUrls: ['./record-add.component.css']
})
export class RecordAddComponent implements OnInit {

	@Input() record: Record = { id: undefined, value: undefined, timestamp: undefined };
	
	constructor(private recordService: RecordService, private location: Location) { }

	ngOnInit() {
	}
	
	save(): void {
		// TODO Error handling.
		this.recordService.addRecord(this.record).subscribe(() => this.goBack());
	}

	goBack(): void {
		this.location.back();
	}

}