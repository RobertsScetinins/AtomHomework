import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppRoutingModule } from './app-routing.module';
import { FormsModule }    from '@angular/forms';
import { HttpClientModule }    from '@angular/common/http';

import { AppComponent } from './app.component';
import { RecordListComponent } from './record-list/record-list.component';
import { RecordAddComponent } from './record-add/record-add.component';
import { RecordEditComponent } from './record-edit/record-edit.component';
import { RecordDetailComponent } from './record-detail/record-detail.component';
import { StatisticsComponent } from './statistics/statistics.component';
import { HomeComponent } from './home/home.component';

@NgModule({
  declarations: [
    AppComponent,
    RecordListComponent,
    RecordAddComponent,
    RecordEditComponent,
    RecordDetailComponent,
    StatisticsComponent,
    HomeComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
